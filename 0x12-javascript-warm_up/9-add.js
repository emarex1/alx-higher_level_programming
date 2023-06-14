#!/usr/bin/node
const arga = process.argv[2];
const argb = process.argv[3];
const a = Math.floor(Number(arga));
const b = Math.floor(Number(argb));
function add (a, b) {
  console.log(a + b);
}
add(a, b);
