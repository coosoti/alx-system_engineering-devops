#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filename = process.argv[3];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  fs.writeFile(filename, body, 'utf-8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
