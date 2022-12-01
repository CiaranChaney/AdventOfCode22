#!/usr/bin/env python3

import string

path_for_input = "./input.txt"
current_calories = 0
highest_calories = 0

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

with open(path_for_input) as file:
    for line in file:
        if has_numbers(line):
            current_calories += int(line.strip())
        elif (current_calories > highest_calories):
            highest_calories = current_calories
            current_calories = 0
        else: current_calories = 0

print(highest_calories)