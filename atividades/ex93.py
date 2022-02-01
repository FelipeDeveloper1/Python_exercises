jogador = {}
gols = []
soma = 0
nome = input('Digite o nome do jogador: ')
partidas = int(input(f'Quantas partidas o {nome} jogou: '))
for i in range(0, partidas):
    gol = int(input(f'Digite quantos gols na {i}: '))
    soma += gol
    gols.append(gol)
jogador['Nome'] = nome
jogador['Partidas'] = partidas
jogador['Gols'] = gols[:]
jogador['Total de gols'] = soma
jogador['tt'] = sum(gols)
print(jogador)
print('=='*15)
for i, c in jogador.items():
    print(f'O campo {i} tem o valor {c}')
print('=='*15)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas')
i = 0
for c in jogador['Gols']:
    print(f'na partida {i}, foi {c} gols')
    i += 1