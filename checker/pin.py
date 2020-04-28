def prime(number):
    number = int(number)
    summ = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            summ += 1
    if summ != 0:
        return False
    return True

def palindrom(s):
    spisok = s.split(' ')
    stroka = ''.join(spisok)
    s1 = stroka[::-1]
    if s1.upper() == stroka.upper():
        return True
    return False

def power(n):
    n = int(n)
    if n & (n - 1):
        return False
    return True

def checkPin(pinCode):
    code = pinCode[0:].split('-')
    if prime(code[0]) and palindrom(code[1]) and power(code[2]):
        return 'Корректен'
    return 'Некорректен'

print(checkPin('7-101-4'))
print(checkPin('11-22-16'))
