#!/usr/bin/node
/*
First constant, first print
*/
'use strict';

const myArgs = process.argv[2];
if (myArgs === undefined) {
  console.log('No argument');
} else {
  console.log(myArgs);
}
