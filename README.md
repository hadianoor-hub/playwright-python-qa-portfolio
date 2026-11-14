# End-to-End UI Test Automation Portfolio (Python + Playwright + Pytest)

Automated test suite built with **Python**, **Playwright**, and **Pytest** using the **Page Object Model (POM)** design pattern.

## Test Coverage
* **Positive Authentication:** Verifies successful login and dashboard redirection.
* **Negative Authentication:** Validates error handling for locked/invalid user accounts.
* **End-to-End Checkout Flow:** Automates product selection, cart badge validation, checkout form submission, and order confirmation.

## Tech Stack
* **Language:** Python 3
* **Framework:** Playwright & Pytest
* **Design Pattern:** Page Object Model (POM)
* **Reporting:** Pytest-HTML

## How to Run Locally
1. Clone the repository and install dependencies:
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```
2. Run tests and generate an HTML report:
   ```bash
   pytest --html=report.html
   ```
