import pytest
import re
from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url(re.compile(r".*/inventory\.html"))

def test_invalid_login_shows_error(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("locked_out_user", "secret_sauce")
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("Sorry, this user has been locked out")

def test_add_item_to_cart_and_checkout(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    page.locator(".shopping_cart_link").click()
    page.locator("[data-test='checkout']").click()
    page.locator("[data-test='firstName']").fill("Hadia")
    page.locator("[data-test='lastName']").fill("Noor")
    page.locator("[data-test='postalCode']").fill("09111")
    page.locator("[data-test='continue']").click()
    page.locator("[data-test='finish']").click()

    expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")
