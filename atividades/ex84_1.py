dados = list()
pessoas = list()
m = me = 0
c = 0
while True:
    dados.append(input('Digite seu nome: '))
    dados.append(int(input('Digite seu peso: ')))
    if len(pessoas) == 0:
        me = dados[1]
        m = dados[1]
    else:
        if dados[1] > m:
            m = dados[1]
        if dados[1] < me:
            me = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    p = input('Deseja continuar? ').upper()
    if p in 'NAO NOP NAH NÃO NO NAUM N NN':
        break
print(f'O maior peso foi de {m} KG ', end='')
for i in pessoas:
    if i[1] == m:
        print(f'[{i[0]}]', end='')
print(''*15)
print(f'O menor peso foi de {me} KG ', end='')
for i in pessoas:
    if i[1] == me:
        print(f'[{i[0]}]', end='')
