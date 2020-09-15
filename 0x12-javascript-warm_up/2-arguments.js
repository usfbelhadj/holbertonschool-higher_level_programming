#!/usr/bin/node
/*
First constant, first print
*/
'use strict';

var myArgs = process.argv.length;
if (myArgs < 3) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
