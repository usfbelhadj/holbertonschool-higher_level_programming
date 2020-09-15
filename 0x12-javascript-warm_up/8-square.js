#!/usr/bin/node
/*
First constant, first print
*/
'use strict';

const myArgs = process.argv[2];
let i;
if (isNaN(myArgs)) {
  console.log('Missing size');
} else {
  for (i = 0; i < myArgs; i++) {
    console.log('X'.repeat(myArgs));
  }
}
