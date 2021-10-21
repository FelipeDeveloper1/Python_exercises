n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
maior = n1
if n2 > n1 and n2 > n3:
    print(f'O maior é {n2}')
elif n3 > n1 and n3 > n2:
    print(f'O maior é {n3}')
else:
    print(f'o maior é {maior}')
menor = n1
if n2 < n1 and n2 < n3:
    print(f'O menor é {n2}')
elif n3 < n1 and n3 < n2:
    print(f'O menor é {n3}')
else:
    print(f'o menor é {menor}')
