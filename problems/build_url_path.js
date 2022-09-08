function buildPath(path, payload) {
  let [url, query] = path.split('?')
  Object.entries(payload).forEach(([k, v]) => {
    url = url.replace(`/:${k}`, `/${v}`)
    query = query.replace(`{${k}}`, v)
  })
  return url + '?' + query
}

console.log(buildPath("https://www.abc.com/:sender/:id?x={x}", { sender: "emre", id: 5, x: 2 }))