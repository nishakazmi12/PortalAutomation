# Selenium POM Automation Framework

## Overview  
This is a Python-based automated testing framework built using Selenium WebDriver and Pytest. It follows the Page Object Model (POM) design pattern to ensure modularity, maintainability, and reusability of test code. The framework supports data-driven testing, generates detailed reports, and captures screenshots on test failures.


## Features  
- Modular Page Object Model architecture  
- Automated test cases implemented with Pytest  
- Configurable test environment via external configuration files  
- Data-driven testing using external test data files  
- Screenshot capture on test failure for easier debugging  
- Detailed HTML reports and logging for test runs  
- Easy test execution via command line or batch file (`run.bat`)


## Tech Stack  
- Python  
- Selenium WebDriver  
- Pytest  
- Logging module  
- HTML test reports (pytest-html or Allure)  
- Git for version control


## Project Structure  

```

├── Configuration/       # Configuration files (URLs, credentials, env settings)
├── Files/               # Alternate automation tests using unittest along with its requirements.txt file
├── Logs/                # Log files generated during test execution
├── Reports/             # Test execution reports (HTML, XML)
├── Screenshots/         # Screenshots captured on failures
├── TestData/            # External test data files (CSV, JSON, Excel)
├── pageObjects/         # Page Object Model classes for UI elements (using absolute xpath just for example)
├── testCases/           # Test scripts organized by feature
├── utilities/           # Helper functions, custom wait methods, logging
├── README.md            # This documentation file
├── requirements.txt     # Python dependencies
└── run.bat              # Windows batch file to execute tests easily

````


## Getting Started  

### Prerequisites  
- Python 3.x installed  
- ChromeDriver (or other browser drivers) matching your browser version  
- Recommended: use a virtual environment

### Installation  
1. Clone this repository:  
```bash
git clone <your-repo-url>
cd <path_of_folder>
````

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Update configuration files (if necessary) in the `Configuration/` folder.

### Running Tests

* To run all tests via Pytest and generate an HTML report:

```bash
pytest testCases/ --html=Reports/report.html
```

* Or simply execute the batch file on Windows by double-clicking:

```bash
run.bat
```

---

## How It Works

* The `pageObjects` folder contains Python classes representing pages or components of the application under test.
* Test scripts in `testCases` import these page objects to interact with the UI in a modular way.
* Configuration files allow switching environments or credentials without code changes.
* `utilities` contains reusable helper methods such as custom waits, logging, and screenshot capture.
* Test data files provide inputs for data-driven testing scenarios.
* Upon test failure, screenshots and logs are saved for debugging.
* Test results are summarized in detailed HTML reports in the `Reports` folder.

---

## Skills Demonstrated

* Automated functional testing with Selenium WebDriver and Python
* Implementation of Page Object Model (POM) design pattern
* Writing maintainable and reusable test code
* Integration with CI/CD pipelines via batch/script execution
* Generating and managing test reports and logs
* Data-driven testing approaches

---

## Contact

For questions or suggestions, feel free to contact me via GitHub or LinkedIn.

---

*Happy Testing!*

```
