sexo = input('Digite seu genero: [m/f]: ').upper()
while sexo != 'M' and sexo != 'F':
    print('Genero invalido em nosso sistema ')
    sexo = input('Digite seu genero novamente: [m/f]: ').capitalize()
if sexo == 'F' or sexo == 'M':
    print('Adicionado em nosso sistema...')
print('Tenha um otimo dia')
