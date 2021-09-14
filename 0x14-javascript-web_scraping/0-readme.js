#!/usr/bin/node
// this script reads and prints the content of a file

const fs = require('fs');
const filename = process.argv[2];

fs.readFile(filename, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
