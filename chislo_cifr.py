def chislo_cifr(p):
    return len(str(p))

print(chislo_cifr(836))

def chislo_cifr_2(p):
    c = str(p)
    n = 0
    for elem in c:
        n += 1
    return n

print(chislo_cifr_2(836))

def chislo_cifr_3(p):
    n = 1
    while p >= 10:
        p = p // 10
        n += 1
    return n

print(chislo_cifr_3(836))