#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    romanToNumber = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, "M": 1000}
    total = 0
    for position in range(len(roman_string)):
        currentLetter = roman_string[position]
        currentValue = romanToNumber[currentLetter]
        if position < len(roman_string) - 1 and currentValue < romanToNumber[roman_string[position + 1]]:
            total -= currentValue
        else:
            total += currentValue
    return total
