// https://www.codewars.com/kata/51c8e37cee245da6b40000bd/solutions/javascript
function solution(input, markers) {
  const exp = new RegExp(`(\\s+)([${markers.join('')}].*)`, 'igm')
  return input.replace(exp, '')
};