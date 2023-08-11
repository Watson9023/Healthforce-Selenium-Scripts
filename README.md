# **Healthforce Selenium Scripts**

## **Table of Contents**

1. [**Prerequisites**](#prerequisites)
2. [**Getting Started**](#getting-started)
   1. [**Setup**](#setup)
   2. [**Running UI Tests**](#running-ui-tests)
   3. [**Running API Tests**](#running-api-tests)
3. [**Project Structure**](#project-structure)
4. [**Test Cases**](/test_cases)
5. [**Documentation**](/documentation)
6. [**Bug Report**](/bug_report.txt)
7. [**Test Coverage Summary**](/test_coverage_summary.md)

## **Prerequisites**

## **Getting Started**

### **Setup**

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Watson9023/Healthforce-Selenium-Scripts.git
   cd Healthforce-Selenium-Scripts

2. Install the required Python packages:
	`pip install -r requirements.txt`

**Running UI Tests**
	To run the UI tests using Selenium WebDriver, navigate to the tests directory and execute:
	python -m unittest discover -s tests

	python -m unittest discover -s tests

**Running API Tests**
	To run the API tests, navigate to the tests directory and execute:

	python api_test_factorial.py

**Project Structure**
The project is structured as follows:

Healthforce-Selenium-Scripts/
│
├── tests/
│   ├── ...
│   ├── api_test_factorial.py
│   └── ...
│
├── test_cases/
│   ├── test_case_factorial.txt
│   └── ...
│
├── documentation/
│   ├── project_documentation.md
│   └── ...
│
├── bug_report.txt
├── test_coverage_summary.md
├── README.md
└── requirements.txt

**Test Cases**
The test_cases directory contains various test cases for the automated tests. Refer to these test cases for more detailed information on the tests performed.

**Documentation**
The documentation directory contains project documentation that explains the purpose, scope, and details of the automated tests.

**Bug Report**
The bug_report.txt file contains a detailed description of any bugs or issues identified during testing.

**Test Coverage Summary**
The test_coverage_summary.md file provides an overview of the test coverage and the percentage of the application code covered by the automated tests.
