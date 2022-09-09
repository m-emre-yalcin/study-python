var lastDigit = function (a, b) {
  if (b == '0') return 1
  const patterns = {
    0: [0],
    1: [1],
    2: [6, 2, 4, 8],
    3: [1, 3, 9, 7],
    4: [6, 4],
    5: [5],
    6: [6],
    7: [1, 7, 9, 3],
    8: [6, 8, 4, 2],
    9: [1, 9],
  }
  // 9007199254740991 < safest values
  const base = a.slice(-1)
  const last = b.slice(-2)
  const res = patterns[base][last % patterns[base].length]
  return res
}
