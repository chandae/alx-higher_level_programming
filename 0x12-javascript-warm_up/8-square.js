#!/usr/bin/node

// Script to print square of size argv[2].

const myArg = process.argv[2];
const char = 'X';

if (isNaN(Number(myArg))) {
  console.log('Missing size');
} else {
  const row = char.repeat(myArg);
  for (let j = 0; j < myArg; j++) {
    console.log(row);
  }
}
