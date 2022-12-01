""""
Author: Ciaran
Date: 01/12/2022

Solving https://adventofcode.com/2022/day/1

Input data contains lines of numbers, 
    -Each set is the amount of calories carried by an elf, 
    -Each set is seperated by an empty line

Part 1:

How many calories in total does the elf with the most calories have?

Solution:
- Read the data in from the input text file
- Check if each line has a number or not
    - If true add the numbner to the current calories count
    - If false
        - If the current number is higher than the highest seen before it becomes the new highet
        - Else the calories are reset to 0
- The highest sum of calories is then printed at the end

"""

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