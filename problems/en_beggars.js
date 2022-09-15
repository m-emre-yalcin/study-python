// https://www.codewars.com/kata/59590976838112bfea0000fa/solutions/javascript
function beggars(values, n) {
  const res = Array(n).fill(0)
  for (let i = 0; i < values.length; i += (n || 1)) {
    let beggar = n
    const slice = values.slice(i, i + n)
    while (beggar) {
      res[beggar - 1] += slice.length ? slice[beggar - 1] || 0 : 0
      beggar--
    }
  }
  return res
}
// solution 2:
function beggars(values, n) {
  const res = Array(n).fill(0)
  for (let i = 0; i < values.length; i++) {
    res[i % n] += values[i]
  }
  return res
}