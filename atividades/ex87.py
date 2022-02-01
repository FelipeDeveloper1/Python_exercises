matriz = list()
pl = []
sc = []
tc = []
sp = mn = soma = 0
for i in range(0, 9):
    matriz.append(int(input(f'Digite o numero na {i}° posição: ')))
for i in range(0, 9):
    #print(matriz[i])
    if i < 3:
        pl.append(matriz[i])
    if i >= 3:
        if i < 6:
            sc.append(matriz[i])
    if i >= 6:
        tc.append(matriz[i])
for num in matriz:
    if num % 2 == 0:
        sp += num
for c in range(0, 3):
    if c == 0:
        mn = sc[0]
    else:
        if sc[c] > mn:
            mn = sc[c]
for cc in range(2, 9, 3):
    print(cc)
    soma += matriz[cc]
print(f'[ {pl[0]} ][ {pl[1]} ][ {pl[2]} ]')
print(f'[ {sc[0]} ][ {sc[1]} ][ {sc[2]} ]')
print(f'[ {tc[0]} ][ {tc[1]} ][ {tc[2]} ]')
print(f'Soma dos pares é: {sp}')
print(f'O maior numero da segunda linha: {mn}')
print(f'A soma da terceira coluna é {soma}')
