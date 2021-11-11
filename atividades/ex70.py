total = 0
adm = c = menor = 0
name = ' '
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = int(input('Digite o preço do produto: '))
    c += 1
    total += preco
    if preco > 1000:
        adm += 1
    if c == 1:
        menor = preco
        name = nome
    else:
        if preco < menor:
            menor = preco
            name = nome
    contin = str(input('Você deseja continuar ? [S/N]: ')).capitalize()
    if contin in 'Nao Não nao n':
        print('Concluido')
        break
print(f'o maior preço é {preco} do produto {name}')
print(f' são {adm} a cima de mil')
print(f'O total é {total}')
