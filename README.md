
# Automation of Automation Excercise website with Python and Playwright


Above repository contains every test case included at https://www.automationexercise.com/test_cases. Most of the test cases were made in accordance with the Page Object Model desing pattern and using Playwright with Python.



## Requirements


* Python
* Pip
* Playwright
* Pytest
* Pytest-Playwright


## Installation


Create virtual environment with ```python -m venv venv``` and activate it with ```.\venv\Scripts\activate```. Then install the requirements with commands below:


```bash
    pip install playwright
```

```bash
    pip install pytest
```


```bash
    pip install pytest-playwright
```


```bash
    playwright install
```


## Run Locally


To run the tests simply type 


```bash
  pytest
```


Tests are set to run in ```--headed``` mode and use chromium by default. Properties can be changed, for example ```--firefox``` or ```--webkit``` if you want to use different browser. 


To run a single test type


```bash
  pytest -k <name of the function>
```

