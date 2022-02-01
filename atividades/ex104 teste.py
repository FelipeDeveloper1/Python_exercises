a = 'aa'
valor = 0
print(type(a))
if type(a) == int:
    valor = int
    print(valor)
    print('numero')
if type(a) == str:
    valor = str
    print('letras')
    print(valor)
p = valor(input('Digite algo: '))
print(p)