#!/usr/bin/python3
#
# Advent of Code 2023
# Day 1, part 1
# https://github.com/krcs/aoc-2023
#
input = "./input.txt"

def read_lines(file):
    result = []

    with open(input,'r') as f:
        while True:
            line = f.readline()

            if len(line)>0:
                result.append(line.strip())

            if not line:
                break
    return result

lines = read_lines(input)

sum = 0

for line in lines:
    result = []
    for c in line:
        if c >= '0' and c <= '9':
            result.append(c)
    sum += int(result[0] + result[-1])

print(sum)

