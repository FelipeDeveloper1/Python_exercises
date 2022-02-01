import random
qj = int(input('Digite quantas sugestões desejas: '))
dados = list()
c = 1
for i in range(0, 6):
    dados.append(random.randint(0, 60))
    if i == 5:
        dados.sort()
        print(f'O {c} jogo: {dados}')
        dados.clear()
        c += 1
        qj -= 1
    if c >= 2:
        while True:
            for a in range(0, 6):
                dados.append(random.randint(0, 60))
                if a == 5:
                    dados.sort()
                    print(f'O {c} jogo: {dados}')
                    dados.clear()
                    c += 1
                    qj -= 1

                if qj < 1:
                    break
print('Boa sorte')