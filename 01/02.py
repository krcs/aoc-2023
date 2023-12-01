#!/usr/bin/python3
#
# Advent of Code 2023
# Day 1, part 2
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

nums = [
  'one',
  'two',
  'three',
  'four',
  'five',
  'six',
  'seven',
  'eight',
  'nine'
]

for line in lines:
    result = []
    word = ""
    for c in line:
        if c >= '0' and c <= '9':
            result.append(c)
            continue

        word += c
        numw = ""
        for i in range(len(word)-1,-1,-1):
            numw = word[i] + numw
            for i, num in enumerate(nums):
                if num == numw:
                    result.append(str(i+1))
                    numw = ""
                    break
            if len(numw) == 0:
                break
    sum += int(result[0]+result[-1])

print(sum)
