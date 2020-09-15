#!/usr/bin/node
/*
First constant, first print
*/
'use strict';

const myArgs = process.argv[2];
if (isNaN(myArgs)) {
  console.log('Not a number');
} else {
  console.log('My number:', myArgs);
}
