# Playwright
Introduction:
  This repo is all about Playwright with Python using POM.
 
Installation Dependencies:
	Python 3.9,
	Pytest-playwright,
	allure-report
	
	
Execution command:
To execute all test cases: 
pytest ./Test_Scripts/
pytest ./Test_Scripts/ --html=pytest_report.html

## setup
python -m venv venv
source venv/bin/activate
.\venv\Scripts\Activate.ps1
venv\Scripts\activate

pip install -r requirements.txt
(might need to install -upgrade pip)
playwright install



to reload the project
add venv to gitignore.