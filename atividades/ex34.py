salario = int(input('Digite seu salario: '))
if salario >= 1250:
    novosalario = salario + salario * 10 / 100
    print(novosalario)
else:
    novosalario = salario * 15 / 100
    print(novosalario)