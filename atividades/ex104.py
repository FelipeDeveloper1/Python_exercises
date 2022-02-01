def leiaint(num= 'digite algo'):
    n1 = input(num)
    if n1.isnumeric():
        n1 = int(n1)
        return n1
    else:
        while True:
            print('\033[031m ISSO NÃO É UM NUMERO')
            n1 = input(num)
            if n1.isnumeric():
                return n1
                break




n1 = leiaint('Digite um numero: ')
print(f'Vccê digitou o numero: {n1}')