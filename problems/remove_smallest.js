function removeSmallest(numbers) {
  let min = { value: Infinity, index: Infinity }
  return numbers.map((n, i) => {
    if (n < min.value) {
      min = {
        value: n,
        index: i
      }
    }
    return n
  }).filter((n, i) => min.index !== i)
}