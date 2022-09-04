function towerBuilder(n) {
  return Array(n).fill().map((_, i) => ' '.repeat(n - i - 1) + '*'.repeat(i * 2 + 1) + ' '.repeat(n - i - 1))
}
console.log(towerBuilder(2))