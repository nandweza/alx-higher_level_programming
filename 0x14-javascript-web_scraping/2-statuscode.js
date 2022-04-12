#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];

request(URL, function (error, response) {
  if (error) {
    console.error('error:', error);
  } else {
    console.log('statusCode:', response && response.statusCode);
  }
});
