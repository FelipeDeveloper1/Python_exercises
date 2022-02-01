pessoas = {}
dados = []
mm = []
media = 0
pam = []
while True:
    pessoas['nome'] = input('Nome: ')
    while True:
        pessoas['sexo'] = input('Sexo [M/F]: ').upper()
        if pessoas['sexo'] in 'F M':
            break
        print('Erro, digite novamente o sexo')
    pessoas['idade'] = int(input('Idade: '))
    media += pessoas['idade']
    dados.append(pessoas.copy())
    if pessoas['sexo'] == 'F':
        mm.append(pessoas['nome'])
    c = input('Deseja continuar ?  [s/n]: ').upper()
    if c in 'N NOP NAO NÃO NO NAUM NAH NA':
        break
media = media / len(dados)
for c, i in enumerate(dados):
    if dados[c]['idade'] > media:
        pam.append(i)

print(dados)
print(f'O grupo tem {len(dados)} pessoas')
print(f'A media de idade foi {media}')
print(f'As mulheres cadastradas foram: ', end='')
for i in mm:
    print(f'{i}', end=', ')
print()
print(pam)
for i, c in enumerate(pam):
    print(f'nome = {pam[i]["nome"]}; sexo = {pam[i]["sexo"]}; idade = {pam[i]["idade"]}')
print('finalizado')