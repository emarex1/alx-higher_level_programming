#!/usr/bin/node

const arg = process.argv[2];
const convertedArg = Math.floor(Number(arg));

if (Number.isNaN(convertedArg)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${convertedArg}`);
}
