def pyramid(n):
    pyr = ''
    j = 0
    i = 0
    while i in range(0, n):
        if n - 1 == i:
            pyr += (' ' * (n - i - 1)) + '/' + ('_' * j) + '\\\n'
        else:
            pyr += (' ' * (n - i - 1)) + '/' + (' ' * j) +  '\\\n'
        j += 2
        i += 1
    return pyr