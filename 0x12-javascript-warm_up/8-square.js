#!/usr/bin/node
const arg = process.argv[2];
const size = Math.floor(Number(arg));

if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  let i; let j = 0;
  let square = '';
  for (i = 0; i < size; i++) {
    for (j = 0; j < size; j++) {
      square += 'X';
    } square += '\n';
  } console.log(square);
}
