#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number matches a given integer

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const ep = process.argv[2];

request(url + ep, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const json = JSON.parse(body);
  console.log(json.title);
});
