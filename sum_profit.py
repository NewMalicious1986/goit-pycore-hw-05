import re
from typing import Callable


def generator_numbers(text: str):
    """
    Extracts numbers from a given text and yields them as floats.
    Args:
        text (str): The input string containing numbers.
    Yields:
        float: The next number found in the text as a float.
    """

    numbers = re.findall(r"\d+\.\d+|\d+", text)

    for number in numbers:
        yield float(number)


def sum_profit(text: str, func: Callable):
    """
    Calculate the sum of profits extracted from the given text using a specified function.
    Args:
        text (str): The input text containing profit information.
        func (Callable): A function that takes a string and returns an iterable of numbers.
    Returns:
        float: The total sum of the profits extracted from the text.
    """

    total = 0.0
    for number in func(text):
        total += number
    return total
