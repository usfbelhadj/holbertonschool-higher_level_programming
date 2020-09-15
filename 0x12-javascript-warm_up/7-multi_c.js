#!/usr/bin/node
/*
First constant, first print
*/
'use strict';

const myArgs = process.argv[2];
let i;
if (isNaN(myArgs)) {
  console.log('Missing number of occurrences');
} else if (myArgs < 0) {

} else {
  for (i = 0; i < myArgs; i++) {
    console.log('C is fun');
  }
}
