tupla = ( int(input('Digite um numero: ')),
 int(input('Digite um numero: ')),
 int(input('Digite um numero: ')),
 int(input('Digite um numero: ')))

print(tupla)
vezes = tupla.count(9)
pt = tupla.index(3) + 1

print(f'foram {vezes} vez(es) que apareceu 9 ')
if 3 in tupla:
    print(f'Foi na posição {pt} que apareceu o primeiro 3')
else:
    print('Não numero 3')

for a in tupla:
    if a % 2 == 0:
        print(f'{a}', end=' ')