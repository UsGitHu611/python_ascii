def my_crib(floor):
    roof = ''
    floors = ''
    j, i = 0, 0

    while i in range(0, floor + 1):
        if floor == i:
            roof += (' ' * (floor - i)) + '/' + ('_' * j) + '\\\n'
        else:
            roof += (' ' * (floor - i)) + '/' + (' ' * j) + '\\\n'
        j += 2
        i += 1

    for i in range(floor):
        if floor - 1 == i:
            floors += '|' + ('_' * (floor * 2)) + '|\n'
        else:
            floors += '|' + (' ' * (floor * 2)) + '|\n'

    return roof + floors