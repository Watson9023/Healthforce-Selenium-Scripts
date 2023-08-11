# Project Documentation

## Introduction
This project involves automating the testing of a web application that calculates the factorial of a given number. The project utilizes Selenium for web automation and Python's unittest framework for test organization and execution.

## Directory Structure
- `base/`: Contains the `Driver` class for browser setup and driver creation.
- `pages/`: Contains page classes for different application pages.
- `tests/`: Contains test scripts and configuration files.
- `test_cases/`: Contains detailed test case documentation.
- `documentation/`: Contains overall project documentation and explanations.

## Test Execution
To execute tests, navigate to the `tests/` directory and run the following command:
python -m unittest discover -s tests


## Bug Report
A bug was identified during testing where the API call to calculate the factorial returns a status code of 500 instead of the expected 200. Details can be found in the "bug_report.txt" file.

## Test Coverage Summary
A summary of test coverage, including the percentage of code covered by automated tests, is provided in the "test_coverage_summary.md" file.


