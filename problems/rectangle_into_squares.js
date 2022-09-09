// https://www.codewars.com/kata/55466989aeecab5aac00003e/solutions/javascript
function sqInRect(m, n) {
  if (m === n) return null
  const squares = []
  while (m && n) {
    const min = Math.min(m, n)
    if (m < n) n = n - min
    else if (n < m) m = m - min
    else {
      m = 0
      n = 0
    }

    squares.push(min)
  }
  return squares
}