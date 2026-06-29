# Playwright Web Framework

A production-grade Python test automation framework built with Playwright and pytest, featuring an integrated **MCP (Model Context Protocol) server** that connects Claude AI directly to the test suite — enabling AI-assisted test analysis, failure triage, and test case authoring as part of the automation workflow.

Built to demonstrate scalable, maintainable quality engineering practices across UI and API layers, with CI/CD integration via GitHub Actions.

---

## AI Integration — MCP Server

The framework includes a custom MCP server (`mcp.server.py`) that exposes test suite context to Claude AI. This enables:

- **Natural-language failure analysis** — ask Claude to interpret test results and identify root causes
- **AI-assisted test authoring** — generate and refine test cases through conversational prompts
- **Live test context awareness** — Claude can read framework structure, fixtures, and test output directly
- **Accelerated maintenance** — use AI assistance to update selectors, refactor page objects, and extend coverage

This integration reflects real-world application of AI-augmented testing workflows, aligned with emerging industry practices in intelligent test automation.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| Browser Automation | Playwright |
| Test Runner | pytest |
| AI Integration | MCP Server + Claude AI |
| Architecture | Page Object Model |
| API Testing | Playwright request context |
| CI/CD | GitHub Actions |

---

## Project Structure

```
playwright_web_framework/
├── pages/                  # Page Object classes
│   ├── base_page.py        # Shared page methods and utilities
│   └── login_page.py       # Login page interactions
├── tests/                  # Test suites
│   ├── conftest.py         # Fixtures, setup, and shared configuration
│   ├── test_login.py       # UI login flow tests
│   └── api_login_test.py   # API layer tests (health check, auth)
├── utils/                  # Helper utilities and shared clients
│   ├── api_client.py       # API request client
│   └── helpers.py          # Shared test helpers
├── mcp.server.py           # MCP server — Claude AI integration
├── .github/workflows/      # GitHub Actions CI pipeline
├── conftest.py             # Root-level fixtures
├── pytest.ini              # pytest configuration
├── requirements.txt        # Dependencies
└── run.py                  # Local test runner script
```

---

## What This Covers

**UI Automation**
- Playwright-driven browser automation with full Page Object Model implementation
- Fixture-based setup and teardown via pytest `conftest.py`
- Reusable base page class with shared interaction methods

**API Testing**
- Dedicated API client for structured request handling
- Health check and authentication endpoint validation
- Pytest markers for test categorisation (`@pytest.mark.smoke`, `@pytest.mark.regression`)

**AI-Augmented Workflows**
- MCP server integration enabling Claude AI to interact with the live test framework
- Supports AI-assisted authoring, triage, and coverage analysis

**CI/CD**
- GitHub Actions pipeline triggers on every push and pull request to `main`
- Test results visible under the Actions tab

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

**Run by marker**

```bash
pytest tests/ -m smoke -v
pytest tests/ -m regression -v
```

**Run a specific file**

```bash
pytest tests/test_login.py -v
pytest tests/api_login_test.py -v
```

---

## CI Pipeline

Tests run automatically on every push and pull request to `main` via GitHub Actions. Results are available under the **Actions** tab in the repository.

---

## Author

**Iryna Shelevii** — Senior QA Automation Engineer | ISTQB CTFL & CT-AI Certified

[LinkedIn](https://linkedin.com/in/irynasheleviiqa) | [GitHub](https://github.com/drajvmixx)