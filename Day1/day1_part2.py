""""
Author: Ciaran
Date: 01/12/2022

Solving https://adventofcode.com/2022/day/1

Input data contains lines of numbers, 
    -Each set is the amount of calories carried by an elf, 
    -Each set is seperated by an empty line

Part 2:

How many calories do the top 3 elves have?

Solution:
- Read the data in from the input text file
- Check if each line has a number or not
    - If true add the number to the current calories count
    - If false
        - The sum is added to the list of calorie sums
- The list is then sorted and the top 3 are printed + summed to find the final total

"""

#!/usr/bin/env python3

import string

path_for_input = "./input.txt"
current_calories = 0
elves_total_calories = []

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

with open(path_for_input) as file:
    for line in file:
        if has_numbers(line):
           current_calories += int(line.strip())
        else:
            elves_total_calories.append(current_calories)
            current_calories = 0

elves_total_calories.sort()

print("3rd : " + str(elves_total_calories[-3]))
print("2nd : " + str(elves_total_calories[-2]))
print("1st : " + str(elves_total_calories[-1]))
print("Total = " + str(elves_total_calories[-1] + elves_total_calories[-2] + elves_total_calories[-3]))
