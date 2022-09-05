#!/usr/bin/node

// Working with command line arguments in JS

if (process.argv.length === 2) {
  console.log('No argument');
}
if (process.argv.length === 3) {
  console.log('Argument found');
}
if (process.argv.length > 3) {
  console.log('Arguments found');
}
