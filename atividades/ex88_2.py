import random
from time import sleep
dados = []
jogos = []
quant = int(input('Digite a quantidade de jogos que deseja: '))
c = 1
while quant >= c:
    cont = 0
    while True:
        n = random.randint(0, 60)
        if n not in dados:
            dados.append(n)
            cont += 1
        if cont >= 6:
            break
    dados.sort()
    jogos.append(dados[:])
    dados.clear()
    c += 1
for i, l in enumerate(jogos):
    print(f'{i+1}: {l}')
    sleep(1)
print('Good luck')