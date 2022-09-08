/**
 * Must be 9x9 board
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function (board) {
  let isValid = true

  // check for rows
  for (const row of board) {
    isValid = isAllUniq(row)
    if (!isValid) return false
  }

  // check for columns
  for (const col of transpose(board)) {
    isValid = isAllUniq(col)
    if (!isValid) return false
  }

  // check for sub boxes
  let nthBox = 9
  while (nthBox > 0 && isValid) {
    const subBox = subBoxArray(board, nthBox)
    isValid = isAllUniq(subBox)
    nthBox--
  }

  return isValid
};

const subBoxArray = (board, block) => {
  const rowStart = Math.floor((block - 1) / 3) * 3
  const rowEnd = rowStart + 3
  const colStart = ((block - 1) % 3) * 3
  const colEnd = colStart + 3

  const rows = board.slice(rowStart, rowEnd)
  const box = rows.map(row => row.slice(colStart, colEnd))
  return box.flat()
}
const transpose = board => board.map((value, col) => board.map((row, j) => row[col]))
const isAllUniq = (arr) => Boolean(arr.every(n => n === "." || arr.filter(m => m === n).length === 1))