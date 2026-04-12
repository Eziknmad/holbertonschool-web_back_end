# Python - Async Comprehension

This project covers asynchronous generators and async comprehensions in Python 3, using the `asyncio` module.

## Learning Objectives

- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

## Requirements

- Python 3.9 on Ubuntu 20.04 LTS
- `pycodestyle` style (version 2.5.x)
- All functions and coroutines must be type-annotated
- All modules and functions must have documentation

## Tasks

### Task 0: Async Generator

**File**: `0-async_generator.py`

Write a coroutine `async_generator` that loops 10 times, asynchronously waits 1 second per iteration, then yields a random float between 0 and 10.

### Task 1: Async Comprehensions

**File**: `1-async_comprehension.py`

Write a coroutine `async_comprehension` that collects 10 random numbers using an async comprehension over `async_generator` and returns the list.

### Task 2: Run time for four parallel comprehensions

**File**: `2-measure_runtime.py`

Write a coroutine `measure_runtime` that executes `async_comprehension` four times in parallel using `asyncio.gather`, measures the total runtime, and returns it. The total runtime is roughly 10 seconds because all four coroutines run concurrently.

## Author

Eziknmad
