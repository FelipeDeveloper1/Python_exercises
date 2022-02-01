dados = list()
pessoa = list()
m = 0
me = 0
maior = list()
menor = list()
while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite seu peso: ')))
    pessoa.append(dados[:])
    dados.clear()
    c = input('Deseja continuar? [S/N]: ').upper()
    if c in 'NAO NOP NÃO N NO':
        break
c = 0
for i in pessoa:
    c += 1
    if c == 1:
        m = i[1]
        me = i[1]
        maior.append(i)
        menor.append(i)
    else:
        if i[1] > m:
            maior.clear()
            m = i[1]
            maior.append(i)
        if i[1] < me:
            menor.clear()
            me = i[1]
            menor.append(i)


print(f'o maior é {maior[0][0]} com o peso {maior[0][1]}')
print(f'O menor é {menor[0][0]} com o peso {menor[0][1]}')
