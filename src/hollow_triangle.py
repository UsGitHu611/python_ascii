def hollow_triangle(n):
    if n == 1:
        return ['#']

    i, j = 1, 1
    res = ['_' * (n - 1) + '#' + '_' * (n - 1)]
    while i < n - 1:
        res.append("_" * (n - i - 1) + '#' + ('_' * j) + '#' + "_" * (n - i - 1))
        i += 1
        j += 2
    res.append('#' * ((n * 2) - 1))
    return res