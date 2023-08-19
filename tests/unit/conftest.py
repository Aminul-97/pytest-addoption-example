# A example of adding argparse-style options to pytest
# By Nick from CoffeeBeforeArch

import pytest
from src.pass_gen import (generate_password)

# Adds the argparse-like option
def pytest_addoption(parser):
    parser.addoption("--length", action="store", default="10", help="Choose a day!")
    parser.addoption("--no_of_chars", action="store", default="7", help="Choose a day!")


# A simple fixture that gets our day_name option
@pytest.fixture
def pass_gen(request):
  no_of_num = int(request.config.getoption("--length"))-int(request.config.getoption("--no_of_chars"))
  password = generate_password(no_of_num, request.config.getoption("--no_of_chars"))
  letters = sum(c.isalpha() for c in password)
  if letters == int(request.config.getoption("--no_of_chars")) and len(password) == int(request.config.getoption("--length")):
     return "OK"
  else:
     return "NOT OK"
