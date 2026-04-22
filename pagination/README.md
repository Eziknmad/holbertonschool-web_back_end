# Pagination

## Description

This project explores how to paginate a dataset using Python. Pagination
is the process of dividing a large dataset into smaller, manageable chunks
called pages. This project covers three different pagination strategies,
each building on the previous one, using a dataset of popular baby names
from New York City.

---

## Learning Objectives

At the end of this project, you should be able to explain to anyone,
without the help of Google:

- How to paginate a dataset with simple `page` and `page_size` parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

---

## Requirements

- All files are interpreted/compiled on **Ubuntu 20.04 LTS** using
  **Python 3.9**
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- All code should use the **pycodestyle** style (version 2.5.*)
- All modules should have documentation
- All functions should have documentation
- All functions and coroutines must be **type-annotated**

---

## Dataset

The dataset used in this project is `Popular_Baby_Names.csv`, which
contains popular baby names from New York City.

### Download the dataset

```bash
curl -o Popular_Baby_Names.csv "https://your-dataset-url-here"
