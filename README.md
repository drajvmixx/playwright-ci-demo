# Playwright Web Framework

A Python-based test automation framework built with Playwright and pytest, demonstrating scalable UI and API testing practices using Page Object Model architecture.

---

## Tech Stack

- **Python 3.11**
- **Playwright** — browser automation
- **pytest** — test runner
- **Page Object Model** — test structure pattern
- **GitHub Actions** — CI/CD integration

---

## Project Structure

```
playwright_web_framework/
├── pages/                  # Page Object classes
│   ├── base_page.py        # Shared page methods
│   └── login_page.py       # Login page interactions
├── tests/                  # Test suites
│   ├── conftest.py         # Fixtures and setup
│   └── test_login.py       # Login flow tests
├── utils/                  # Helper utilities
├── .github/workflows/      # GitHub Actions CI pipeline
├── requirements.txt
├── pytest.ini
└── run.py
```

---

## What This Covers

- UI test automation using Playwright with Python
- Page Object Model for maintainable, reusable test components
- Fixture-based setup and teardown via pytest `conftest.py`
- Automated test execution on every push via GitHub Actions
- Designed to extend with API test coverage (in progress)

---

## Running Locally

**Install dependencies**

```bash
pip install -r requirements.txt
playwright install chromium
```

**Run all tests**

```bash
pytest tests/ -v
```

**Run a specific test file**

```bash
pytest tests/test_login.py -v
```

---

## CI Pipeline

Tests run automatically on every push and pull request to `main` via GitHub Actions. Results are available under the Actions tab in the repository.

---

## Roadmap

- [ ] Add API test layer using `requests` or Playwright `request` context
- [ ] Expand UI coverage beyond login flows
- [ ] Add HTML test reporting
- [ ] Add test data management via fixtures

---

## Author

Iryna Shelevii — [LinkedIn](https://linkedin.com/in/irynasheleviiqa) | [GitHub](https://github.com/drajvmixx)