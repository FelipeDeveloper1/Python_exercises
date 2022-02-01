import random
jogos = int(input('Quantos jogos deseja sortear? '))
numeros = list()
c = jogos
cont = 1
for i in range(0, 6):
    n = random.randint(0, 60)
    numeros.append(n)
    if i == 5:
        numeros.sort()
        print(f'Jogo {cont} foi: {numeros} ')
        numeros.clear()
        cont += 1
if c > 1:
    while c > 1:
        for i in range(0, 6):
            n = random.randint(0, 60)
            numeros.append(n)
            if i == 5:
                numeros.sort()
                print(f'Jogo {cont} foi: {numeros}')
                numeros.clear()
                cont += 1
                c -= 1

