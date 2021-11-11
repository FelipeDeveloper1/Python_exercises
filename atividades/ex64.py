num = int(input('Digite seu numero: '))
soma = 0
quantidadedenumeros = 0
while num != 999:
    soma += num
    num = int(input('Digite seu numero: '))
    quantidadedenumeros += 1
print(f'A soma {soma}')
print(f'quantidade de numeros digitados foi: {quantidadedenumeros} ')
print('Fim do programa')