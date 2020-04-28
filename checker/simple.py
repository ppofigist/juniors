def prime(number):
    summ = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            summ += 1
    if summ != 0:
        return 'Составное'
    return 'Простое'

print(prime(16))