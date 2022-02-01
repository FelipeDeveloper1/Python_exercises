listaa = list()
lista = list()
listaa.append(lista)
pl = list()
sl = list()
tl = list()
for num in range(0, 9):
    lista.append(int(input('Digite um numero: ')))
for i in range(0, 3):
    pl.append(lista[i])
for i in range(3, 6):
    sl.append(lista[i])
for i in range(6, 9):
    tl.append(lista[i])
print(lista)
print('[  {}  ][  {}  ][  {}  ] ' .format(pl[0], pl[1], pl[2]))
print('[  {}  ][  {}  ][  {}  ] ' .format(sl[0], sl[1], sl[2]))
print('[  {}  ][  {}  ][  {}  ] ' .format(tl[0], tl[1], tl[2]))
print(f'{listaa[0][1]}')