# ES6 Promises

JavaScript ES6 Promises project covering async patterns: Promise creation, chaining, error handling, `async`/`await`, and try/catch.

## Learning Objectives

- Promises (how, why, and what)
- How to use the `then`, `resolve`, `catch` methods
- How to use every method of the Promise object
- Throw / Try
- The `await` operator
- How to use an `async` function

## Requirements

- Node 20.x.x / npm 9.x.x
- ESLint with airbnb-base rules
- Jest for testing

## Files

| File | Description |
|------|-------------|
| `utils.js` | Utility functions `uploadPhoto` and `createUser` (used by tasks 3, 6) |
| `0-promise.js` | `getResponseFromAPI` — returns a Promise |
| `1-promise.js` | `getFullResponseFromAPI(success)` — resolves `{status:200, body:'Success'}` or rejects with error |
| `2-then.js` | `handleResponseFromAPI(promise)` — chains `.then`, `.catch`, `.finally` |
| `3-all.js` | `handleProfileSignup` — `Promise.all` on uploadPhoto + createUser; logs `body firstName lastName` |
| `4-user-promise.js` | `signUpUser(firstName, lastName)` — resolved Promise with `{firstName, lastName}` |
| `5-photo-reject.js` | `uploadPhoto(filename)` — rejected Promise with `Error: filename cannot be processed` |
| `6-final-user.js` | `handleProfileSignup(firstName, lastName, fileName)` — `Promise.allSettled`, returns `[{status, value}]` |
| `7-load_balancer.js` | `loadBalancer(chinaDownload, USDownload)` — `Promise.race`, returns first settled value |
| `8-try.js` | `divideFunction(numerator, denominator)` — throws `Error('cannot divide by 0')` if denominator is 0 |
| `9-try.js` | `guardrail(mathFunction)` — try/catch/finally, returns queue with result and `'Guardrail was processed'` |

## Setup

```bash
npm install
npm run full-test
```
