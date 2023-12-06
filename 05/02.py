#!/usr/bin/python3
#
# Advent of Code 2023
# Day 5, part 2
# https://github.com/krcs/aoc-2023
#
import sys
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

test = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

#lines = test.split('\n')

def get_data(lines):
    seeds = list(map(int, lines[0].split(': ')[1].split(' ')))
    section = 0

    sections = {
        'seed-to-soil map:' : 1,
        'soil-to-fertilizer map:' : 2,
        'fertilizer-to-water map:': 3,
        'water-to-light map:' : 4,
        'light-to-temperature map:' : 5,
        'temperature-to-humidity map:': 6, 
        'humidity-to-location map:': 7
    }

    section_values = {
        1 : [],
        2 : [],
        3 : [],
        4 : [],
        5 : [],
        6 : [],
        7 : []
    }

    for line in lines[2:]:
        if line in sections:
            section = sections[line]
            continue

        if len(line) == 0:
            continue

        section_values[section].append(list(map(int,line.split(' '))))
    return (seeds, section_values)


seeds, categories = get_data(lines)

s = []

for idx in range(0,len(seeds),2):
    s.append([seeds[idx], seeds[idx]+seeds[idx+1]])

seed_ranges = sorted(s, key=lambda e: e[0])

###

low_location = sys.maxint
for r in seed_ranges:
    seed = r[0]
    while seed <= r[1]:
        stack = [seed]
        for c in categories:
            current_value = stack[-1]
            test = False
            d = current_value
            for line in categories[c]:
                source_start = line[1]
                source_end = line[1]+line[2]-1

                destination_start = line[0]
                destination_end = line[0]+line[2]-1

                offset = current_value - source_start
                if current_value >= source_start and current_value <= source_end:
                    d = destination_start+offset

            stack.append(d)
        if stack[-1] < low_location:
            low_location = stack[-1]
        seed += 1

print(low_location)


