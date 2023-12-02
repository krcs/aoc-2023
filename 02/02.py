#!/usr/bin/python3
#
# Advent of Code 2023
# Day 2, part 2
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

test = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

sum = 0

for line in lines:# test.split('\n'):
    p = line.split(':')
    id = int(p[0].split(' ')[1])
    sets = p[1].split(';')
    cubes = [0,0,0]
    for set in sets:
        for a in set.split(','):
            l = a.strip().split(' ')
            n = int(l[0])
            if l[1] == 'red':
                if cubes[0] < n:
                    cubes[0] = n
            elif l[1] == 'blue':
                 if cubes[1] < n:
                    cubes[1] = n
            elif l[1] == 'green':
                if cubes[2] < n:
                    cubes[2] = n

    sum += cubes[0] * cubes[1] * cubes[2]

print(sum)
