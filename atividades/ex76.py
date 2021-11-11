list = ('frango', 30, 'Carne',  35, 'cereal', 15, 'feijao', 8, 'picanha', 100, 'vinho', 80)
print('-'*60)
print(' '*20 + 'LISTA DE PREÇOS')
print('-'*60)
a = -2
b = -1
while True:
    a += 2
    b += 2
    print(f'{list[a]}' + '.'*15 + f'{list[b]}R$ ')
    if a == 10 and b == 11:
        break
print('-'*60)