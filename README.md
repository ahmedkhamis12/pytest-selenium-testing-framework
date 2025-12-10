# PyTest Selenium Testing Framework

A lightweight example project showing API and UI testing with pytest,
requests, and selenium.

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running tests
- All tests: `pytest`
- API tests only: `pytest tests/test_api_users.py`
- UI test only: `pytest tests/test_ui_login.py`

## Notes
- API tests are stubbed to avoid external network calls (see `framework/api_client.py`).
- The UI test uses Selenium. If Chrome/Chromium is unavailable, the fixture
  falls back to a dummy driver so the test can still pass. Install Chrome to
  exercise a real browser run. 
