resp = 's'
media = soma = quantid = 0
menor = maior = 0
while resp in 'S s sim Sim':
    n1 = int(input('Digite um numero: '))
    quantid += 1
    soma += n1
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if quantid == 1:
        maior = n1
        menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
media = soma / quantid
print(f'A soma de tudo foi {soma}, quantidade de numero digitado foi {quantid} e a media foi {media}')
print(f'O maior numero foi {maior} e o menor foi {menor}')
print('Tenha um otimo dia')