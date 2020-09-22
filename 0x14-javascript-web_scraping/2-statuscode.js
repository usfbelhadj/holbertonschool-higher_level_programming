#!/usr/bin/node
/*
Display the status code of a GET request
*/
const request = require('request');
request.get(process.argv[2], function (error, response) {
  if (error) {
    console.error('error:', error);
  }
  console.log('code:', response && response.statusCode);
});
