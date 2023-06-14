#!/usr/bin/node
const arg = process.argv[2];
const x = Math.floor(Number(arg));

if (Number.isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  let counter = 0;
  while (counter < x) {
    console.log('C is fun');
    counter++;
  }
}
