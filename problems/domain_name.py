def domain_name(url):
    return url.replace('https://','').replace('http://','').replace('www.','').split('.')[0]

print(domain_name('http://www.github.com'))