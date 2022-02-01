import random
from time import sleep
from operator import itemgetter
dados = {}
ordem = []
for c in range(1, 5):
    num = random.randint(0, 6)
    dados[f'{c}'] = num
    print(f'{c} jogador com {dados[f"{c}"]}')
    sleep(1)
print('Ranking dos Jogadores')
ordem = sorted(dados.items(), key=itemgetter(1), reverse=True)
for c, i in enumerate(ordem):
    print(f'{c+1} jogador {i[0]} com {i[1]} ')
    sleep(1)
