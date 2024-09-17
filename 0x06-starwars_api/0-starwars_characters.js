#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (err, resp, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const characters = JSON.parse(body).characters;

  const characterPromises = characters.map((character) => {
    return new Promise((resolve, reject) => {
      request(character, (err, resp, body) => {
        if (err) reject(err);
        resolve(JSON.parse(body).name);
      });
    });
  });

  Promise.all(characterPromises)
    .then((names) => {
      names.forEach((name) => console.log(name));
    })
    .catch((err) => console.log(err));
});
