Python Selenium — Page Object Example with Allure and Selenium Grid

Requirements
- Python 3.10+
- Docker & Docker Compose

Quick setup
1. Create and activate a virtual environment
```bash
   python -m venv .venv
   source .venv/bin/activate
```
2. Install dependencies
```bash
   pip install -r requirements.txt
```
3. Start Selenium standalone Chrome in docker
```bash
   docker-compose up -d
```
or start grid
```bash
   java -jar selenium-server-4.41.0.jar standalone
```
4. Run tests in headless mode and open Allure report
```bash
   pytest
   allure serve reports/allure
```
5. Serve Allure report (requires Allure CLI)
```bash
   brew install allure
   allure serve reports/allure
```

Environment
- `SELENIUM_GRID_URL` default `http://localhost:4444/wd/hub`
- `BROWSER` default `chrome`
- `HEADLESS` default `1` (set to `0` to run headed)

Notes
- Tests use a Remote WebDriver pointed at `SELENIUM_GRID_URL` so you can replace it with a real Grid endpoint.