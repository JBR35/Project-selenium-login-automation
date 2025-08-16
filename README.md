# Selenium Login Automation with Allure Reports

## Overview
A Selenium automation project in Python for testing login functionality using **Page Object Model (POM)** and **pytest** with Allure HTML reports.

**Test Site:** [The Internet - Herokuapp](https://the-internet.herokuapp.com/login)

## Features
- Page Object Model (POM)
- Multiple login test cases
- Headless Chrome execution
- Automatic driver management (`webdriver-manager`)
- Allure HTML report generation

## Setup Instructions
1. Clone the repository:
```bash
git clone https://github.com/raju/selenium-login-automation.git
cd selenium-login-automation
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run tests with Allure report:
```bash
pytest --alluredir=reports
```

5. View the HTML report:
```bash
allure serve reports
```

## Tools Used
- Python 3.x
- Selenium 4.x
- Pytest
- Allure Reports
- Webdriver Manager

## Author
Your Name
