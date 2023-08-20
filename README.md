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
There are two arguments you can pass to the test.
1. `--length` = Provide the length of the password
2. `--no_of_chars` = Provide the number of alphabets for the password

The default values for the above arguments are as follows,

| Args | Default value |
| --- | --- |
| `--length` | 10 |
| `--no_of_chars` | 7 |

You can run the test in default mode by using the command below,
```cmd
pytest "tests\unit\test_addoption.py"
```

You can also pass arguments like the ones below,
```cmd
pytest --length=10 --no_of_chars=6 "tests\unit\test_addoption.py"
```