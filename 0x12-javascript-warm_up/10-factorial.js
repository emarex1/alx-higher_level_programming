#!/usr/bin/node
const n = Math.floor(Number(process.argv[2]));
function factorial (n) {
  if (Number.isNaN(n)) {
    return 1;
  } else if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(n));
