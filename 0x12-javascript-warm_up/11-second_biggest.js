#!/usr/bin/node

// script that finds the second biggest integer in list of arguments passed to it.

if (process.argv.length < 4) {
  console.log('0');
} else {
  const args = process.argv.slice(2, -1);
  args.sort();
  console.log(args[1]);
}
