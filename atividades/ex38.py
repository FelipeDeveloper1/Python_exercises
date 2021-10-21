n1 = int(input('Digite um numero inteiro qualquer: '))
n2 = int(input('Digite outro numero inteiro qualquer: '))
maior = n1
if n2 > n1:
    print(f'\033[34m {n2} é o maior valor e esta em segundo lugar')
elif n1 == n2:
    print(f'\033[33m {n1} e {n2} são iguais \033[m')
else:
    print(f'\033[34m {maior} é o maior e esta em primeiro lugar')
print('Tenha um otimo dia')
