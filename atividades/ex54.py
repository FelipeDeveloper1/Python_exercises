pessoas = 0
for i in range(0, 7):
    data = int(input('Digite sua data de nascimento: '))
    if data >= 2004:
        pessoas += 1
print(f'{pessoas} pessoas tem menos de 18 anos')
