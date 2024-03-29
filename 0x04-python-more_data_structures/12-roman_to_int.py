#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return (0)
    if not isinstance(roman_string, str):
        return (0)
    v = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    total = 0
    for ch in range(len(roman_string)):
        cur_ch = roman_string[ch]
        if ch < len(roman_string) - 1 and v[roman_string[ch + 1]] > v[cur_ch]:
            total -= v[cur_ch]
        else:
            total += v[cur_ch]
    return (total)
