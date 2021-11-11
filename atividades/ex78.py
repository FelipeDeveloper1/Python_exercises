laco = []
for b in range(1, 6):
    laco.append(int(input(f'Digite o {b}° valor: ')))
maior = menor = 0
print(laco)
for a in range(0, len(laco)):
    if a == 0:
        maior = laco[a]
        menor = laco[a]
    else:
        if laco[a] > maior:
            maior = laco[a]
        if laco[a] < menor:
            menor = laco[a]
print(f'O maior é: {maior}, o menor é {menor}')