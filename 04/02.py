#!/usr/bin/python3
#
# Advent of Code 2023
# Day 4, part 2
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

test = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

lines = test.split('\n')

def get_parsed_data(lines):
    result = {}
    for line in lines:
        sections = line.split(':')
        card = sections[0].split(' ')[-1]
        numbers = sections[1].split('|')
        w = []
        for number in numbers[0].strip().split(' '):
            if len(number) > 0:
                w.append(int(number))
        c = []
        for number in numbers[1].strip().split(' '):
            if len(number) > 0:
                c.append(int(number))
        result[card] = [w, c]
    return result


cards = get_parsed_data(lines);
wins = {}
for card in cards:
    points = 0
    counter = 0
    for w in cards[card][0]:
        for c in cards[card][1]:
            if w == c:
                counter += 1
    wins[int(card)] = counter

result = []


for i in list(wins.keys()):
    result.append(i)
    copy = list(range(i+1, wins[i]+2))
    result += copy
    break

print(result)
