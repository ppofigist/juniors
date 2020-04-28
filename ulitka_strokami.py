way = '@>>>V>>>'
simbol = way[0]
vpravo = 0
vlevo = 1
vivod = ''
first_string = True
for i in range(1, len(way)):
    if way[i] != 'V':
        vivod += simbol
        if way[i] == '>':
            vpravo += 1
        elif way[i] == '<':
            vlevo += 1
    else:
        vivod += simbol
        sdvig = vpravo - vlevo - 1
        vpravo = 1
        vlevo = 1
        print(' ' * sdvig, end='')
        print(vivod)
        vivod = ''


