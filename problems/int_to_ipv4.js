function int32ToIp(int32) {
  let ipv4 = []
  let bits = Number(int32).toString(2)
  if (bits.length !== 32) bits = '0'.repeat(32 - bits.length, '0').concat(bits)

  for (const i in bits) {
    if (i % 8 === 0) {
      const octat = bits.substr(i, 8)
      const int = parseInt(octat, 2)
      ipv4.push(int)
    }
  }
  return ipv4.join('.')
}

console.log(int32ToIp(117355108))

// for int32 = 117355108
// : expected '223.214.76.4' to equal '6.254.178.100'

// for int32 = 1500990336
// : expected '178.238.151.0' to equal '89.119.75.128'