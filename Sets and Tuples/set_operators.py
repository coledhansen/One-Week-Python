webdev = {'SQL', 'css', 'html', 'js', 'python'}
data = {'R', 'SQL', 'python'}

## intersection
print(webdev & data)
    # {'python', 'SQL'}

## union
print(webdev | data)
    # everything
    # {'python', 'R', 'html', 'css', 'SQL', 'js'}

## difference
print(webdev - data)
    # what values are only UNIQUE in left side
    # {'css', 'html', 'js'}
print(data - webdev)
    # {'R'}

## alternate ways using set method
print(
    webdev.intersection(data),
    webdev.union(data),
    webdev.difference(data)
)
