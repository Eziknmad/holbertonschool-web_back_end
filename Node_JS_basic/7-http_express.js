const express = require('express');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];
const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const chunks = ['This is the list of our students'];
  countStudents(database)
    .then(() => {
      res.send(chunks.join('\n'));
    })
    .catch((err) => {
      chunks.push(err.message);
      res.send(chunks.join('\n'));
    });
});

app.listen(1245);

module.exports = app;
