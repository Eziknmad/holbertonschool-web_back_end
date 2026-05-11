# NodeJS Basics

## Description
Introduction to Node.js — running JavaScript on the server side, reading files, handling HTTP requests, and building REST APIs with Express.

## Requirements
- Node 20.x.x
- Ubuntu 20.04 LTS
- All files end with a new line and use `.js` extension

## Setup
```bash
npm install
```

## Files

| File | Description |
|------|-------------|
| `0-console.js` | `displayMessage(string)` — prints a string to STDOUT |
| `1-stdin.js` | Program that reads user input from stdin |
| `2-read_file.js` | `countStudents(path)` — reads CSV synchronously and logs student counts |
| `3-read_file_async.js` | `countStudents(path)` — async version, returns a Promise |
| `4-http.js` | Basic HTTP server on port 1245 using Node's `http` module |
| `5-http.js` | HTTP server with `/` and `/students` routes using `http` module |
| `6-http_express.js` | Basic HTTP server on port 1245 using Express |
| `7-http_express.js` | Express server with `/` and `/students` routes |
| `full_server/` | Organized Express server with controllers and routes |

## Full Server Structure
```
full_server/
├── server.js
├── utils.js
├── controllers/
│   ├── AppController.js
│   └── StudentsController.js
└── routes/
    └── index.js
```

## Usage

### Run individual files
```bash
node 0-console.js
node 1-stdin.js
node 4-http.js
node 5-http.js database.csv
node 6-http_express.js
node 7-http_express.js database.csv
```

### Run full server
```bash
npm run dev
```

### Test endpoints
```bash
curl localhost:1245/
curl localhost:1245/students
curl localhost:1245/students/CS
curl localhost:1245/students/SWE
```

### Run tests
```bash
npm run test
npm run full-test
```

## Author
Kevin Galarza Arzon
