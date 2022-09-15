// https://www.codewars.com/kata/596f72bbe7cd7296d1000029/train/javascript
function deepCount(a) {
  return a.reduce((a, b) => a + (Array.isArray(b) ? deepCount(b) : 0), a.length)
}