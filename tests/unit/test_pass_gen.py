import pytest
from src.pass_gen import generate_password


@pytest.fixture
def pass_gen(request) -> tuple:
    """
    Fixture to accept the length and number of characters input from the command line.
    :param request: pytest request object

    :return: Tuple of length and number of alpha num characters
    """
    # Taking passed args for length and number of chars
    length = int(request.config.getoption("--length"))
    no_of_alphanum = int(request.config.getoption("--no_of_alphanum"))

    yield length, no_of_alphanum


# Test function
def test_pass_gen(pass_gen) -> None:
    """
    Test function to test the password generator.

    :param pass_gen: Fixture to accept the length and number of characters input from the command line.

    :return: None
    """
    length, no_of_alphanum = pass_gen

    # Generate the password
    password = generate_password(length, no_of_alphanum)

    # Find number of alphanumeric characters
    num_of_alpha = sum(c.isalnum() for c in password)

    # Check if the password matches the requirements
    assert num_of_alpha == no_of_alphanum and len(password) == length
