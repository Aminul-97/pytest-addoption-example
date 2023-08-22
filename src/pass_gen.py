import string
import random
from itertools import cycle


def generate_password(length: int, num_alphanumeric: int) -> str:
    """
    Generate a password of a given length with a given number of alphanumeric characters.

    :param length: Total number of characters in the password
    :param num_alphanumeric: Number of alphanumeric characters in the password

    :return: Password string
    """
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits

    # Ensure the number of alphanumeric characters is within bounds
    num_alphanumeric = max(0, min(num_alphanumeric, length))

    # Calculate the number of remaining characters needed
    num_remaining = length - num_alphanumeric

    # Generate a list of alphanumeric characters
    alphanumeric_chars = random.sample(
        lowercase_letters + uppercase_letters + digits, num_alphanumeric
    )

    # Generate a list of remaining characters
    remaining_chars = random.choices(
        string.ascii_letters + string.digits, k=num_remaining
    )

    # Combine the two lists and shuffle
    password_chars = alphanumeric_chars + remaining_chars
    random.shuffle(password_chars)

    # Create the password string
    password = "".join(password_chars)
    return password


# if __name__ == "__main__":
#     password = generate_password2(16, 10)
#     print(password)
