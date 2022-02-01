exp = str(input('Digite uma expressão: '))
lista = []
for val in exp:
    if val == '(':
        lista.append('(')
    elif val == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressão valida')
else:
    print('Expressão invalida')