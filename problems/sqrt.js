/*
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

 * @param {number} x
 * @return {number}
 */
var mySqrt = function (x) {
  let base = 0

  while (Infinity) {
    // distance with the x
    const dist = x - Math.floor(base * base)

    // compare the distance
    if (dist == 0) return base
    else if (dist < 0) return base - 1

    base += 1
  }
}

var mySqrt2 = function (a) {
  if (a == 0) return 0

  var x, x1 = a / 2;

  while (x !== x1) {
    x = x1;
    x1 = (x + (a / x)) / 2;
  }
  return x;
}

console.log(mySqrt2(5))