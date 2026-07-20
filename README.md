# QA SauceDemo Selenium Python Pytest

[![Selenium Python Tests](https://github.com/encristian/QA-SauceDemo-Selenium-Python-Pytest/actions/workflows/selenium-tests.yml/badge.svg)](https://github.com/encristian/QA-SauceDemo-Selenium-Python-Pytest/actions/workflows/selenium-tests.yml)

This is a UI automation testing project built with **Python**, **Selenium WebDriver** and **Pytest**.

The project tests the SauceDemo web application:

https://www.saucedemo.com/

---

## Project Highlights

- 18 automated UI tests
- Page Object Model structure
- Reusable Pytest browser fixture
- Config and test data separation
- HTML test report generation
- Screenshots on test failure
- GitHub Actions CI pipeline
- Automated test execution on every push to `main`

---

## Project Purpose

The purpose of this project is to practice UI test automation using Selenium with Python.

This project covers:

- Selenium WebDriver tests
- Pytest test framework
- Page Object Model structure
- Login tests
- Products tests
- Cart tests
- Checkout tests
- Test data and config separation
- HTML test reports
- Screenshots on test failure
- GitHub Actions CI
- Git and GitHub version control

---

## Technologies Used

- Python
- Selenium WebDriver
- Pytest
- pytest-html
- Git
- GitHub
- GitHub Actions
- Visual Studio Code

---

## Project Structure

```text
QA-SauceDemo-Selenium-Python-Pytest/
│
├── .github/
│   └── workflows/
│       └── selenium-tests.yml
│
├── pages/
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── login_page.py
│   └── products_page.py
│
├── tests/
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_login_smoke.py
│   └── test_products.py
│
├── utils/
│   ├── config.py
│   └── test_data.py
│
├── conftest.py
├── pytest.ini
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Test Scenarios Covered

### Login Tests

- Verify login page is displayed
- Verify valid login
- Verify invalid login error message

### Products Tests

- Verify Products page is displayed after login
- Verify product list is displayed
- Verify first product details are displayed
- Verify Add to Cart updates cart badge

### Cart Tests

- Verify Cart page is displayed
- Verify product is displayed in cart
- Verify product details are displayed in cart
- Verify product can be removed from cart
- Verify Continue Shopping redirects to Products page

### Checkout Tests

- Verify Checkout Information page is displayed
- Verify checkout form fields are displayed
- Verify empty checkout form shows error message
- Verify valid checkout information opens Checkout Overview page
- Verify Checkout Overview displays product and price information
- Verify complete order shows confirmation message

---

## Page Object Model

The project uses the Page Object Model pattern.

Each page has its own class:

- `LoginPage` handles login page actions and validations
- `ProductsPage` handles products page actions and validations
- `CartPage` handles cart page actions and validations
- `CheckoutPage` handles checkout page actions and validations

This makes the tests cleaner, easier to read and easier to maintain.

---

## Test Data and Config

The project uses separate files for config and test data.

- `config.py` stores application URLs
- `test_data.py` stores usernames, passwords, checkout data and expected messages

This keeps test data separate from test logic.

---

## Test Reports

This project uses `pytest-html` to generate HTML test reports.

Run tests:

```bash
pytest
```

After execution, the HTML report is generated here:

```text
reports/report.html
```

If a test fails, a screenshot is automatically saved here:

```text
reports/screenshots/
```

The `reports/` folder is ignored by Git because it contains generated files.

---

## Continuous Integration

This project uses GitHub Actions to run the Selenium Pytest test suite automatically.

The workflow runs on:

- Push to `main`
- Pull request to `main`

The workflow performs the following steps:

- Checks out the repository
- Sets up Python
- Installs project dependencies
- Runs the Pytest test suite
- Uploads the HTML test report as a GitHub Actions artifact

Workflow file:

```text
.github/workflows/selenium-tests.yml
```

---

## How to Run the Tests

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Open the project folder

```bash
cd QA-SauceDemo-Selenium-Python-Pytest
```

### 3. Create virtual environment

```bash
python -m venv .venv
```

### 4. Activate virtual environment

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Run tests

```bash
pytest
```

---

## Current Test Status

```text
18 passed
```

Latest test execution:

```text
All UI automation tests passed successfully.
```

---

## What I Learned

Through this project, I practiced:

- Writing automated UI tests with Selenium
- Using Pytest as a test framework
- Creating a Page Object Model structure
- Using reusable browser fixtures with `conftest.py`
- Separating config and test data
- Testing login, products, cart and checkout flows
- Generating HTML test reports
- Taking screenshots on test failure
- Creating a GitHub Actions workflow
- Running automated tests in CI
- Using Git commits
- Structuring a QA Automation portfolio project

---

## Author

Created as part of my QA Automation portfolio.