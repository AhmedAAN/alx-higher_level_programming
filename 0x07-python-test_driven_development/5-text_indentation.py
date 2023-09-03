#!/usr/bin/python3
"""Defines a text printing and detection function."""


def text_indentation(text):
    """Print a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If the text is not string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    newLineFlag = 1
    for letter in text:
        if letter == "\n":
            print("")
            newLineFlag = 1
        elif newLineFlag == 0:
            print(letter, end ="")
            if (letter == '.' or letter == '?' or letter == ':'):
                print("")
                print("")
                newLineFlag = 1
        else:
            if letter != " ":
                print(letter, end = "")
                newLineFlag = 0
