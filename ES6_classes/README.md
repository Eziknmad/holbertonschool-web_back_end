# ES6 Classes

JavaScript ES6 class syntax project covering object-oriented programming concepts.

## Learning Objectives

- How to define a class in ES6
- How to add methods to a class
- Why and how to add a static method to a class
- How to extend a class from another
- Metaprogramming and symbols

## Requirements

- Node 20.x.x / npm 9.x.x
- ESLint with airbnb-base rules
- Jest for testing

## Tasks

| File | Description |
|------|-------------|
| `0-classroom.js` | `ClassRoom` class — accepts `maxStudentsSize` stored as `_maxStudentsSize` |
| `1-make_classrooms.js` | `initializeRooms` — returns array of 3 `ClassRoom` objects (sizes 19, 20, 34) |
| `2-hbtn_course.js` | `HolbertonCourse` — getters/setters with `TypeError` type validation for `name`, `length`, `students` |
| `3-currency.js` | `Currency` — getters/setters + `displayFullCurrency()` returning `name (code)` |
| `4-pricing.js` | `Pricing` — imports `Currency`, getters/setters, `displayFullPrice()`, static `convertPrice()` |
| `5-building.js` | `Building` — abstract class that throws `Error` if subclass doesn't implement `evacuationWarningMessage` |
| `6-sky_high.js` | `SkyHighBuilding` — extends `Building`, overrides `evacuationWarningMessage` |
| `7-airport.js` | `Airport` — uses `Symbol.toStringTag` so `toString()` returns `[object code]` |
| `8-hbtn_class.js` | `HolbertonClass` — uses `Symbol.toPrimitive`: Number cast → size, String cast → location |
| `9-hoisting.js` | Fixed hoisting bug — moved class declarations before usage, corrected constructor/getter bugs |
| `10-car.js` | `Car` — uses `Symbol.species` so `cloneCar()` returns a new instance of the same subclass |

## Setup

```bash
npm install
npm run full-test
```
