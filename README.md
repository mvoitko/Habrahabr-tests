# Habrahabr-tests
BDD Test scenarios for Habrahabr with Python 3.5.

This framework tests the basic functionality of Habrahabr web-app using page object model.


Based on:
- Behave - BDD testing https://behave.readthedocs.org
- Selenium - web applications testing https://selenium-python.readthedocs.org
- PyHamcrest - matchers and assertions https://pyhamcrest.readthedocs.org

## Setup

```shell
git clone git@github.com:mvoitko/Habrahabr-tests.git
cd path/to/Habrahabr-tests
pip install -r requirements.txt
```

## Running tests

```shell
behave # run all feature files
behave features/ # run all feature files in the given folder
behave features/search.feature # run the search.feature file only
behave -t=smoke # run only features/scenarios with @smoke tag
```