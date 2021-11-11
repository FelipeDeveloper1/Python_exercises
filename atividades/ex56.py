media = 0
qm = 0
divisor = 0
hmv = 0
name = ''
for i in range(1, 5):
    print(f'--- {i}° pessoa ---')
    nome = input('Digite seu nome: ').capitalize()
    sexo = input('Sexo [H/F]: ').capitalize()
    idade = int(input('Digite sua idade: '))
    if sexo == 'H' and i == 1:
        hmv = idade
        name = nome
    else:
        if i > hmv:
            hmv = idade
            name = nome
    if sexo == 'F' and idade < 20:
        qm += 1
    media += idade
    divisor = i
media = media / divisor
print(f'O homem mais velho tem {hmv} anos e seu nome é {name}')
print('{:.1f}'.format(media))
print(f'São {qm} mulhere(s) com menos de 20 anos')