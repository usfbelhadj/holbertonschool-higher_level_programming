#!/usr/bin/node
/*
First constant, first print
*/
'use strict';

function fac (num) {
  if (isNaN(num) || num < 2) {
    return 1;
  } else {
    return num * fac(num - 1);
  }
}
console.log(fac(process.argv[2]));
