#!/usr/bin/node
/*
First constant, first print
*/
'use strict';

const myArgs = process.argv.length;
if (myArgs < 3) {
  console.log('undefined is undefined');
} else if (myArgs === 2) {
  console.log(process.argv[2], 'is undefined');
} else {
  console.log(process.argv[2], 'is', process.argv[3]);
}
