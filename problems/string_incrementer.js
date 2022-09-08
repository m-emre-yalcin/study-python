// https://www.codewars.com/kata/54a91a4883a7de5d7800009c/solutions/javascript
function incrementString(string) {
  const reg = /[0-9]+$/g
  const strEndNum = string.match(reg)
  if (strEndNum === null) return string.concat('1')

  let num = +strEndNum[0] + 1
  let len = strEndNum[0].length > String(num).length ? strEndNum[0].length : String(num).length
  let zeros = '0'.repeat(len)
  num = (zeros + num).slice(-len)

  return string.replace(reg, num)
}

// one clever solution:
// let incrementString = str => str.replace(/([0-8]|\d?9+)?$/, (e) => e ? + e + 1 : 1)