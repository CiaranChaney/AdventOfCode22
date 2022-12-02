""""
Author: Ciaran
Date: 02/12/2022

Solving https://adventofcode.com/2022/day/2

Input data contains the moves of the opponent and the elf, 
    -The first char is the opponents move (A,B,C)
    -The second char is the elfs move (X,Y,Z)

Part 2:

X = lose, Y = draw, Z = win

Scores:
Rock = 1, Paper = 2, Scissors = 3
Win = 6, Draw = 3, Loss = 0

What is the elf's score at the end of the game?

Solution:
- Read the data in from the input text file
- A + X = loss + 3, A + Y = draw + 1, A + Z = win + 2
- B + X = loss + 1, B + Y = draw + 2, B + Z = win + 3
- C + X = loss + 2, C + Y = draw + 3, C + Z = win + 1
"""

#!/usr/bin/env python3

import string

PATH_FOR_INPUT = "./input.txt"

elf_score = 0

def win(choice_score):
    global elf_score
    elf_score += 6 + choice_score

def draw(choice_score):
    global elf_score
    elf_score += 3 + choice_score

def loss(choice_score):
    global elf_score
    elf_score += choice_score

with open(PATH_FOR_INPUT) as file:
    for line in file:
        line_stripped = line.strip()

        if(line_stripped.startswith("A") and line_stripped.endswith("X")):
            loss(3)
        elif(line_stripped.startswith("A") and line_stripped.endswith("Y")):
            draw(1)
        elif(line_stripped.startswith("A") and line_stripped.endswith("Z")):
            win(2)
        elif(line_stripped.startswith("B") and line_stripped.endswith("X")):
            loss(1)
        elif(line_stripped.startswith("B") and line_stripped.endswith("Y")):
            draw(2)
        elif(line_stripped.startswith("B") and line_stripped.endswith("Z")):
            win(3)
        elif(line_stripped.startswith("C") and line_stripped.endswith("X")):
            loss(2)
        elif(line_stripped.startswith("C") and line_stripped.endswith("Y")):
            draw(3)
        elif(line_stripped.startswith("C") and line_stripped.endswith("Z")):
            win(1)

print(elf_score)
        