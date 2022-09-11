// https://www.codewars.com/kata/53b138b3b987275b46000115/solutions/javascript
function compareVersions(version1, version2) {
  const v1 = version1.split('.').map(Number)
  const v2 = version2.split('.').map(Number)
  for (let i = 0; i < Math.max(v1.length, v2.length); i++) {
    const n1 = v1[i] || 0
    const n2 = v2[i] || 0

    if (n1 === n2) continue

    return n1 > n2
  }
  return true
}