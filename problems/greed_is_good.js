// https://www.codewars.com/kata/5270d0d18625160ada0000e4/javascript
function score(dice) {
  const scored = new Set()
  const count = n => dice.filter(num => num === n).length
  const points = {
    '3=>1': 1000,
    '3=>2': 200,
    '3=>3': 300,
    '3=>4': 400,
    '3=>5': 500,
    '3=>6': 600,
    '1=>1': 100,
    '1=>5': 50
  }
  return dice.reduce((a, b) => {
    if (scored.has(b)) return a

    let nth = count(b)
    while (nth > 0) {
      const key = nth => `${nth}=>${b}`
      if (key(nth) in points) {
        a += points[key(nth)]
        nth = 0
      }
      else if (key(1) in points) a += points[key(1)]
      nth--
    }
    scored.add(b)
    return a
  }, 0)
}