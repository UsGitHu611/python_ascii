def dot(n, m):
    res = ''
    sep = '+' + ('---+' * n) + '\n'
    for _ in range(m):
        res += sep + ('| o ' * n) + '|' '\n'
    return res + sep[:-1]