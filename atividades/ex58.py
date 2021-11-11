import random
n = int(input('Digite um numero: '))
num = random.randint(0, 10)
tentativas = 0
while n != num:
    num = random.randint(0, 10)
    print(f'Você errou, o numero foi {num}')
    n = int(input('Digite o numero ate acerta: '))
    tentativas += 1
if n == num:
    print(f'Finalmente, você acertou, {n} = {num}')

print(f'NUMEROS DE TENTATIVAS: {tentativas}')