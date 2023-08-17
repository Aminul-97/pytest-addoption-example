# A example of adding argparse-style options to pytest
# By Nick from CoffeeBeforeArch

import pytest
from src.day_code import (day_code)

# Adds the argparse-like option
def pytest_addoption(parser):
    parser.addoption("--day_name", action="store", default="null", help="Choose a day!")


# A simple fixture that gets our day_name option
@pytest.fixture
def day_name(request):
  return day_code(request.config.getoption("--day_name"))
