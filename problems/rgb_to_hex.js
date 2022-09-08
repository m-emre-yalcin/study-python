function rgb(r, g, b) {
  const to16 = n => {
    if (n < 0) return '00'
    else if (n > 255) return 'FF'

    const hex = Number(n).toString(16).toUpperCase()
    if (hex.length == 1) return '0' + hex
    else return hex
  }
  return Object.values(arguments).map(to16).join('')
}