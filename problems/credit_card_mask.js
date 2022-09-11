function maskify(cc) {
  return cc.replace(/(\w*)(\w{4}$)/g, (m, g1, g2) => '#'.repeat(g1.length) + g2)
}
