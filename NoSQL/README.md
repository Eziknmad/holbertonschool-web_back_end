# NoSQL

## Description
This project covers the fundamentals of NoSQL databases using MongoDB. It includes MongoDB shell scripts for basic CRUD operations and Python scripts using PyMongo for programmatic database interaction.

## Learning Objectives
- What NoSQL means
- Difference between SQL and NoSQL
- What ACID means
- What document storage is
- Types of NoSQL databases
- Benefits of a NoSQL database
- How to query, insert, update, and delete in a NoSQL database
- How to use MongoDB

## Requirements
- Ubuntu 20.04 LTS
- MongoDB 4.4
- Python 3.9
- PyMongo 4.8.0
- pycodestyle 2.5.*

## Files

| File | Description |
|------|-------------|
| `0-list_databases` | Lists all databases in MongoDB |
| `1-use_or_create_database` | Creates or switches to database `my_db` |
| `2-insert` | Inserts a document with `name: "Holberton school"` into `school` collection |
| `3-all` | Lists all documents in `school` collection |
| `4-match` | Lists all documents with `name="Holberton school"` |
| `5-count` | Displays the number of documents in `school` collection |
| `6-update` | Adds `address: "972 Mission street"` to documents with `name="Holberton school"` |
| `7-delete` | Deletes all documents with `name="Holberton school"` |
| `8-all.py` | Python function that lists all documents in a collection |
| `9-insert_school.py` | Python function that inserts a new document based on kwargs |
| `10-update_topics.py` | Python function that updates all topics of a school by name |
| `11-schools_by_topic.py` | Python function that returns schools having a specific topic |
| `12-log_stats.py` | Python script that prints stats about Nginx logs in MongoDB |

## Usage

### MongoDB Shell Scripts
```bash
cat 0-list_databases | mongo
cat 2-insert | mongo my_db
```

### Python Scripts
```bash
./8-main.py
./12-log_stats.py
```
