"""
Raising Your Own Errors Lecture written by Joe Manlove

created 7/20/2020
revised 10/22/25 to include this docstring, fix other docstrings, and use isinstance instead of type
"""

# Goal 1: learn to raise our own errors.
# Factorial recursion video: https://youtu.be/LgprFL4SsaA

def factorial(n: int):
    """
    Returns the factorial of a non-negative integer. Note, 0! = 1.

    Args:
        n (int): The non-negative integer to calculate the factorial of.
    """

    # check if n can be treated as an integer
    # in the video I used "type(n) != int"
    # isinstance is a bit safer as it allows for object inheritance
    if not isinstance(n, int):
        raise TypeError("Not of integer type, n must be a positive integer.")
    if n < 0:
        raise ValueError("n must be a positive integer.")

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def input_integer(prompt:str='Please, input an integer.\n'):
    """
    Read a string from standard input. The trailing newline is stripped.

    The prompt string, if given, is printed to standard output without a trailing newline before reading input.
    Input is cast to an integer and returned, non-integer inputs raise TypeErrors.

    Keyword Args:
        prompt (str): The prompt string printed into the console.
    """

    user_input = input(prompt)

    # startwith
    # isnumeric


input_integer()
