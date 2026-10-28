"""
Raising Your Own Errors Lecture written by Joe Manlove

created 7/20/2020
revised 10/22/25 to include this docstring, fix other docstrings, and use isinstance instead of type
"""

# Goal 1: learn to raise our own errors.
# Factorial recursion video: https://youtu.be/LgprFL4SsaA

def factorial(n):
    """
    Returns the factorial of a non-negative integer. Note, 0! = 1.

    Args:
        n (int): The non-negative integer to calculate the factorial of.
    """

    # n = input_integer()
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

    # While true loop to keep trying if the user enters incorrect values
    while True:
        # try the user input prompt
        try:
            user_input = input(prompt)
            print(f"You entered: '{user_input}'")

            # If user input is negative
            if user_input.startswith("-"):
                # create wrong_input boolean and assign false
                wrong_input = True
                # raise custom ValueError
                raise ValueError(f"Invalid input :'{user_input}'. Must be a positive integer.")

            # If user input is not numeric
            elif not user_input.isnumeric():
                # Create wrong_input boolean and assign True
                wrong_input = True
                # Raise custom TypeError
                raise TypeError(f"Invalid input :'{user_input}'. Not of integer type.")

            else:
                # Assign false to wrong_input
                wrong_input = False
                # int cast user_input
                user_input = int(user_input)
                # Run the factorial method using user input, assign to final_factorial variable
                final_factorial = factorial(user_input)

        # Except handle the TypeError
        except TypeError as error:
            print(error)

        # Except handle the ValueError
        except ValueError as error:
            print(error)

        # Else print invalid input message and break loop
        else:
            print(f"Valid Input '{user_input}' processed.")
            break

        finally:
            # print err message if wrong input boolean is True
            if wrong_input:
                print("Try again\n")
            # Or print success message and results
            else:
                print(f"\nFactorial of '{user_input}': {final_factorial}")
                print("Process completed successfully.")

        return user_input

input_integer()