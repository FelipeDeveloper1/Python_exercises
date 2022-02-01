lista = []
pares = []
impares = []
while True:
    num = int(input('Digite um numero: '))
    lista.append(num)
    c = input('Deseja continuar? [S/N]: ').upper()
    if c in 'NAO NOP NAO NAH N NAO NÃO':
        break
for val in lista:
    if val % 2 == 0:
        pares.append(val)
    else:
        impares.append(val)
c = input('Deseja ver seus numeros e impar ? [S/N]: ').upper()
if c in 'SIM SS CLARO SIM SI YEAH YES SS YEP YE SSS':
    print(pares)
    print(impares)
else:
    print('Tudo bem, não sera mostrado')
print(lista)



