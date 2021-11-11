soma = 0
for i in range(1, 501):
    if i % 3 == 0:
        soma += i
        #print(i)
        print(soma)
print(f'a soma de todos os numeros foi {soma}')