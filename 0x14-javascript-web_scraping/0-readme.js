#!/usr/bin/node
/*
eads and prints the content of a file.
*/
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function read (err, data) {
  if (err) throw err;
  console.log(data);
});
