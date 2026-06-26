# QA SauceDemo Selenium Python Pytest

This is a UI automation testing project built with **Python**, **Selenium WebDriver** and **Pytest**.

The project tests the SauceDemo web application:

https://www.saucedemo.com/

---

## Project Purpose

The purpose of this project is to practice UI test automation using Selenium with Python.

This project will include:

* Selenium WebDriver tests
* Pytest test framework
* Page Object Model
* Login tests
* Products tests
* Cart tests
* Checkout tests
* HTML test reports
* Git and GitHub version control

---

## Technologies Used

* Python
* Selenium WebDriver
* Pytest
* pytest-html
* Git
* GitHub

---

## Project Structure

```text
QA-SauceDemo-Selenium-Python-Pytest/
│
├── pages/
│
├── tests/
│   └── test_login_smoke.py
│
├── utils/
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## How to Run Tests

### 1. Create virtual environment

```bash
python -m venv .venv
```

### 2. Activate virtual environment

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run tests

```bash
pytest
```

### 5. Run tests with HTML report

```bash
pytest --html=reports/report.html
```

---

## Current Test Status

```text
12 passed
```

---

## Author

Created as part of my QA Automation portfolio.
