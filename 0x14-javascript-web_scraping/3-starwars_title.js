#!/usr/bin/node
/*
 Star Wars movie where the episode number matches a given integer
*/
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  console.log(JSON.parse(body).title);
});
