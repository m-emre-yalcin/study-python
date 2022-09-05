function findUniq(arr) {
  const sorted = arr.sort((a, b) => a - b)
  const [a, b] = sorted
  return a === b ? sorted.pop() : a
}
console.log(findUniq([1, 1, 1, 1, 4, 1, 1]))