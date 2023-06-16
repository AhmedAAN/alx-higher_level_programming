#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return (0)
    if not isinstance(roman_string, str):
        return (0)
    values = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    total = 0
    for ch in range(len(roman_number)):
        current_ch = roman_number[ch]
        if ch < len(roman_number) - 1 and values[roman_number[ch + 1]] > values[current_ch]:
            total -= values[current_ch]
        else:
            total += values[current_ch]
    return (total)
