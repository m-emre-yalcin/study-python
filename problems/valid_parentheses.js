function validBraces(braces) {
  const pairs = {
    '[': ']',
    '{': '}',
    '(': ')'
  }
  const trace = []
  for (let i = 0; i < braces.length; i++) {
    // opening
    if (braces[i] in pairs) {
      trace.push(braces[i])
    }
    // closing
    else {
      // nothing opened before
      if (trace.length === 0) return false
      const last = trace[trace.length - 1]
      if (pairs[last] === braces[i]) trace.pop()
      else break
    }
  }
  return trace.length === 0
}