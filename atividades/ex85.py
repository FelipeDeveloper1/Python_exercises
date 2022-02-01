par = list()
impar = list()
num = list()
for i in range(1, 8):
    num.append(int(input(f'Digite o {i} numero: ')))
for a in num:
    if a % 2 == 0:
        par.append(a)
    else:
        impar.append(a)

print(num)
print(par)
print(impar)