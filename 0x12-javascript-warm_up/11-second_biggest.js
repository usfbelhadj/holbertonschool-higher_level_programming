#!/usr/bin/node
/*
First constant, first print
*/
'use strict';

if (process.argv.length == 2 || process.argv.length == 3) {
  console.log('0');
} else {
  console.log(process.argv.slice(2).sort((a, b) => b - a)[1]);
}
