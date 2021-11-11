c = ''
cont = 0
h = mm = pm = 0
maior = menor = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [H/F]: ')).capitalize()
    cont += 1
    if cont == 1:
        maior = idade
        menor = idade
    else:
        if idade > maior:
            maior = idade
        if idade < menor:
            menor = idade
    if sexo == 'F' and idade < 20:
        mm += 1
    elif sexo == 'H':
        h += 1
    if idade < 18:
        pm += 1
    c = str(input('Quer continuar ? [S/N]: ')).capitalize()
    if c in 'Nao N Não':
        break
print(f'São {mm} que tem menos de 20 anos')
print(f'São {h} homens cadastrados')
print(f' São {pm} pessoas com menos de 18 anos')
print(f'O maior é {maior} e o menor é {menor}')