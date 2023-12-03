#!/usr/bin/python3
#
# Advent of Code 2023
# Day 3, part 1
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

test = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
.......755
...$.*....
.664.598.."""

#lines =test.split('\n')

def isSymbol(c):
    return c != '.'

def get_part_number(start, end, line_number, lines):
    current_line = lines[line_number]
    num = int(current_line[start:end+1])
    if start-1 >= 0:
        if isSymbol(current_line[start-1]):
            return num
    if end+1 < len(current_line):
        if isSymbol(current_line[end+1]):
            return num

    s = start
    if s-1 >= 0:
        s -= 1
    e = end
    if e + 1 < len(current_line):
        e += 1

    if line_number > 0:
        for i in range(s, e+1):
            x = lines[line_number-1][i]
            if isSymbol(x):
                return num

    if line_number < len(lines)-1:
        for i in range(s, e+1):
            x = lines[line_number+1][i]
            if isSymbol(x):
                return num

    return 0

result = 0

for n, line in enumerate(lines):
    start = -1
    end = -1
    for i, c in enumerate(line):
        if c.isdigit(): 
            if start == -1:
                start = i
            end = i
        elif start != -1:
            num = get_part_number(start,end, n, lines)
            result += num
            start = -1
            end = -1
    if start != -1:
        num = get_part_number(start,end, n, lines)
        result += num

print("Result:", result)
