a = ''
b = str(input('Digite algo: '))
if b.find(','):
    b = b.replace(',', '.')
    a += f'{b}'

a += '* 2 '
print(eval(a))
print(type(a))