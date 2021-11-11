numeros= []

c = 0
nd = []
while True:
    c += 1
    num = int(input(f'Digite o {c} valor: '))
    if num not in numeros:
        numeros.append(num)
        print('Valor adicionado')
    else:
        print('Valor ja existente, não será adicionado')
    continua = input('Deseja continuar? [S/N] ').capitalize()
    if continua in 'N NAO NA NAUM Nop No Nah':
        break
numeros.sort()
menor = numeros[0]
maior = numeros[-1]

print(numeros)
print(maior, menor)