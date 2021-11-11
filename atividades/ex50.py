soma = 0
for a in range(1, 7):
    n = int(input('Digite um numero inteiro: '))
    if n % 2 == 0:
        soma += n
if soma == 0:
    print('Não há numeros pares para somar')
print(soma)