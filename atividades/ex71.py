valor = int(input('Digite o valor que sera sacado: '))
total = valor
cedula = 50
quanti = 0
while True:
    if total >= cedula:
        total -= cedula
        quanti += 1
    else:
        if quanti > 0:
            print(f'As notas foram {cedula} e foram usadas {quanti}')
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        quanti = 0
        if total == 0:
            break