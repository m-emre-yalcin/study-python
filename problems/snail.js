const snail = arr => {
  const finalArray = [];
  while (arr.length) {
    finalArray.push(...arr.shift())
    arr.forEach(row => finalArray.push(row.pop()))
    arr.reverse().forEach(row => row.reverse())
  }
  return finalArray
}

snail([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])