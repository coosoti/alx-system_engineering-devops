#!/usr/bin/node
//  this script writes a string to a file

const fs = require('fs');
const argv = process.argv;
const filename = argv[2];
const newContent = argv[3];

fs.writeFile(filename, newContent, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
