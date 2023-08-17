This repo contains the sample code for the article **A comprehensive guide on Pytest Addoption**

## Code
The source code is a simple Python script that finds the code of a weekday and can be found at `src/day_code.py`. 

Unit Tests can be found at `tests/unit/test_addoption.py`

Also, you'll find a test configuration file at `tests/unit/conftest.py`

## Requirements
* Python (3.8+)

Please create a virtual environment and activate it.

Install the dependencies via the `requirements.txt` file using 

```commandline
pip install -r requirements.txt
```
If you don't have Pip installed please follow instructions online on how to do it.

## How To Run the Tests
To run the  Tests, from the root of the repo run
```commandline
pytest --day_name [YOUR OPTION] "tests\unit\test_addoption.py" 
```
Here the available `OPTIONS` are `sat`, `sun`, `mon`, `tue`, `wed`, `thu`, `fri`

For example,

```commandline
pytest --day_name sun "tests\unit\test_addoption.py" 
```