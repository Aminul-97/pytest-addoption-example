import pytest
from src.pass_gen import (generate_password)


# A simple fixture that gets our day_name option
@pytest.fixture
def pass_gen(request):
  
  # Taking passed args for length and number of chars
  length = int(request.config.getoption("--length")) 
  no_of_char = int(request.config.getoption("--no_of_chars"))
  
  # if no_of_char >= length then,
  # Set no_of_num = 0 and no_of_char = length
  if length <= no_of_char:
     no_of_char = length
     no_of_num =  0
  else:
     no_of_num = length - no_of_char 

  # Generate the password
  password = generate_password(no_of_num, no_of_char)

  # Find number of alphabetic characters
  letters = sum(c.isalpha() for c in password)

  # Check if the password matches the requirements
  if letters == no_of_char and len(password) == length:
     yield "OK"
  else:
     yield "NOT OK"

# Test function
def test_pass_gen(pass_gen):
     assert pass_gen == "OK"