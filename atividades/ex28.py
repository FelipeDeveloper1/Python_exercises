import random
numerodigitado = int(input('Digite um numero de um a cinco: '))
n1 = random.randint(1, 5)
if numerodigitado == n1:
    print(f'Você digitou {numerodigitado} e o resultado foi {n1}, você ganhou')
else:
    print(f'Você digitou {numerodigitado} e o resultado foi {n1}, o computador ganhou')
    