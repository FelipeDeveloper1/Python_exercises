import random
num = []
def aleatorio():
    c = 5
    while c != 0:
        n = random.randint(0, 10)
        if n not in num:
            num.append(n)
        else:
            if n in num:
                n += random.randint(0, 100)
                num.append(n)
        c -= 1


aleatorio()
print(num)
def somapar():
    soma = 0
    a = 0
    while a < len(num):
        if num[a] % 2 == 0:
            soma += (num[a])
        a += 1
    print(f'A soma de todos os pares foram {soma}')
somapar()