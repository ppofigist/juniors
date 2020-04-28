def palindrom(s):
    spisok = s.split(' ')
    stroka = ''.join(spisok)
    s1 = stroka[::-1]
    if s1.upper() == stroka.upper():
        return 'Палиндром'
    return 'Не палиндром'

print(palindrom('а роза упала на лапу азора'))