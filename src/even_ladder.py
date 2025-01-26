def even_ladder(n):
    if n <= 1:
        return ''
    return "\n".join([f'{i}' * i for i in range(0, n + 1, 2)]).strip()
