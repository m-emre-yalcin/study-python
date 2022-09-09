// https://www.codewars.com/kata/54d4c8b08776e4ad92000835/solutions/javascript
var isPP = function (n) {
  for (const root of getPrimes(Math.ceil(Math.sqrt(n)))) {
    const base = Math.round(Math.pow(n, 1 / root) * 100) / 100

    if (isFloat(base) === false && parseInt(base ** root) === n) return [base, root]
  }

  return null
}
function isFloat(n) {
  return n % 1 !== 0
}
function getPrimes(max) {
  var sieve = [], i, j, primes = [];
  for (i = 2; i <= max; ++i) {
    if (!sieve[i]) {
      // i has not been marked -- it is prime
      primes.push(i);
      for (j = i << 1; j <= max; j += i) {
        sieve[j] = true;
      }
    }
  }
  return primes;
}
