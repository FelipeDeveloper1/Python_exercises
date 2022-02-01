lista = []
c = 0
while True:
    c += 1
    lista.append(int(input('Digite o valor: ')))
    confi = str(input('Deseja continuar: [S/N]: ')).upper()
    if confi in 'NAO NOP NO NAO N NAH':
        break

lista.sort(reverse=True)
print(lista)
print(f'Total de numeros digitados: {c}')
if 5 in lista:
    print('Cinco esta na lista')
else:
    print('Não há cinco na lista')