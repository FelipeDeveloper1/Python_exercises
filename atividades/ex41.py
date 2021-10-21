idade = int(input('Digite sua idade: '))
if idade == 9 or idade < 14:
    print(f'{idade} anos é mirim')
elif idade == 14 or idade <19:
    print(f'{idade} anos é infantil')
elif idade ==19 or idade < 20:
    print(f'{idade} anos é Senior ')
else:
    print(f'{idade} anos é master')
