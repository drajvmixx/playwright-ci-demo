# Playwright Web Framework

A Python-based test automation framework built with Playwright and pytest, demonstrating scalable UI and API testing practices using the Page Object Model (POM) architecture.

## Tech Stack

* Python 3.13
* Playwright — Browser automation
* pytest — Test runner and fixtures
* Page Object Model (POM) — Test architecture
* Requests/API Client — API testing
* GitHub Actions — CI/CD integration

---

## Project Structure

```text
playwright_web_framework/
│
├── pages/                     # Page Object Models
│   ├── __init__.py
│   ├── base_page.py           # Shared page functionality
│   └── login_page.py          # Login page interactions
│
├── tests/                     # Test suites
│   ├── __init__.py
│   ├── conftest.py            # Pytest fixtures
│   ├── test_login.py          # UI login tests
│   └── api_login_test.py      # API login tests
│
├── utils/                     # Helper utilities
│   ├── __init__.py
│   ├── api_client.py          # API request wrapper
│   └── helpers.py
│
├── .github/
│   └── workflows/             # GitHub Actions CI pipeline
│
├── .gitignore
├── pytest.ini                 # Pytest configuration
├── requirements.txt           # Project dependencies
├── run.py                     # Test runner
├── mcp.server.py
└── README.md
```

---

## Features

### UI Testing

* Playwright browser automation
* Page Object Model (POM) design pattern
* Reusable page components
* Pytest fixtures for setup and teardown
* Cross-browser execution support

### API Testing

* API client abstraction layer
* Response validation
* Authentication and login endpoint testing
* Reusable API fixtures

### CI/CD

* Automated test execution through GitHub Actions
* Runs on every push and pull request
* Easy integration into development workflows

---

## Sample Test Coverage

### UI

* Successful login validation
* Invalid credentials validation
* Empty login form validation

### API

* Login endpoint validation
* Response status code verification
* Response payload validation

---

## Running Locally

### Install dependencies

```bash
pip install -r requirements.txt
playwright install chromium
```

### Run all tests

```bash
pytest tests/ -v
```

### Run UI tests

```bash
pytest tests/test_login.py -v
```

### Run API tests

```bash
pytest tests/api_login_test.py -v
```

### Run tests in headed mode

```bash
pytest tests/ --headed
```

---

## CI Pipeline

Tests run automatically on every push and pull request through GitHub Actions.

Test results and workflow logs are available under the **Actions** tab of the repository.

---

## Future Enhancements

* Add HTML reporting (pytest-html)
* Add Allure reporting
* Expand API test coverage
* Add test data management fixtures
* Add parallel execution support
* Add environment-based configuration

---

## Author

**Iryna Shelevii**

* GitHub: https://github.com/drajvmixx
* LinkedIn: [www.linkedin.com/in/iryna-shelevii](http://www.linkedin.com/in/iryna-shelevii)

---

## Notes

The following directories are generated automatically and excluded from source control:

```text
__pycache__/
.pytest_cache/
.venv/
venv/
```
