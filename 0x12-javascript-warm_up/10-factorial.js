#!/usr/bin/node
/*
First constant, first print
*/
'use strict';

const num = process.argv[2];
let i; let sum = 1;
for (i = num; i >= 1; i--) {
  sum = sum * i;
}
console.log(sum);
