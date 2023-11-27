#!/opt/node/bin/node
/*
    Advent of Code 2023
    Day x, part x
    https://github.com/krcs/aoc-2023
*/

const fs = require('fs');

let lines = fs.readFileSync('./input.txt', 'UTF-8')

lines = lines.trim().split('\n');

for (let line of lines) {
    console.log(line);
}
