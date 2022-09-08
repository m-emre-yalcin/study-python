// https://www.codewars.com/kata/55c6126177c9441a570000cc/train/javascript
function orderWeight(string) {
  const numToWeight = str => str.split('').reduce((a, b) => a + +b, 0)
  return string.split(' ').sort((a, b) => numToWeight(a) - numToWeight(b) || a > b || -(a < b)).join(' ')
}