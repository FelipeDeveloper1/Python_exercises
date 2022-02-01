jogadores = {}
gol = []
info = []
while True:
    jogadores['nome'] = input('Digite o nome do jogador: ')
    jogadores['partidas'] = int(input(f'Quantas partidas o {jogadores["nome"]} jogou: '))
    for i in range(0, jogadores['partidas']):
        gol.append(int(input(f'Quantos gols no {i}° jogo: ')))
        jogadores['gols'] = gol[:]
    total = 0
    for i in gol:
        total += i
    jogadores['total'] = total
    info.append(jogadores.copy())
    gol.clear()
    c = input('Deseja continuar ? [S/N]: ').upper()
    if c in 'NÃO NOP NAO N NAUM NO NOP NAH NN':
        break
print(info)
print('=='*30)
print('cod nome', ' '*15, 'gol', ' '*15, 'total')
for c, i in enumerate(info):
    print(f'{c} {info[c]["nome"]}',' '*15,f'{info[c]["gols"]}',' '*15, f'{info[c]["total"]}')

while True:
    dad = int(input('Qual jogador você deseja ver os dados: '))
    if dad > len(info):
        print('ERRO, jogador não existente no sistema, digite novamente')
        dad = int(input('Qual jogador você deseja ver os dados: '))
    if dad < len(info):
        print(f'Mostrando dados do jogador {info[dad]["nome"]}')
        for i in range(0, info[dad]['partidas']):
            print(f'no jogo {i} foi feito {info[dad]["gols"][i]}')
    if dad == 999:
        break


