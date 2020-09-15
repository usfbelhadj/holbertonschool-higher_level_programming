#!/usr/bin/node
/*
First constant, first print
*/
'use strict';

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

console.log(add(process.argv[2], process.argv[3]));
