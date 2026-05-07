# ES6 Data Manipulation

JavaScript ES6 data manipulation project covering `map`, `filter`, `reduce`, typed arrays, Set, and Map data structures.

## Learning Objectives

- How to use `map`, `filter`, and `reduce` on arrays
- Typed arrays (`ArrayBuffer`, `DataView`, `Int8`)
- The `Set`, `Map`, and `WeakMap` data structures

## Requirements

- Node 20.x.x / npm 9.x.x
- ESLint with airbnb-base rules
- Jest for testing

## Tasks

| File | Description |
|------|-------------|
| `0-get_list_students.js` | Returns array of student objects (id, firstName, location) |
| `1-get_list_student_ids.js` | Returns array of ids using `map`; returns `[]` if not an array |
| `2-get_students_by_loc.js` | Filters students by city using `filter` |
| `3-get_ids_sum.js` | Sums all student ids using `reduce` |
| `4-update_grade_by_city.js` | Filters by city then adds grade using `filter` + `map`; `N/A` if no grade |
| `5-typed_arrays.js` | Creates `ArrayBuffer`/`DataView` with Int8 at position; throws if out of range |
| `6-set.js` | Converts array to `Set` |
| `7-has_array_values.js` | Returns boolean: all array elements exist in the Set |
| `8-clean_set.js` | Returns `-`-joined string of set values starting with `startString` (suffix only) |
| `9-groceries_list.js` | Returns a `Map` of groceries with name → quantity |
| `10-update_uniq_items.js` | Updates Map entries with quantity 1 → 100; throws if not a Map |

## Setup

```bash
npm install
npm run full-test
```
