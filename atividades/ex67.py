n = int(input('Digite um numero: '))
tabu = res = 0
while True:
    for i in range(1, 11):
        tabu = n * i
        print(f'Nxi = {tabu}')
    res = int(input('Deseja continuar? (digite numero negativo caso não queira):  '))
    if res < 0:
        break
    n = int(input('Digite o numero: '))
print('Tenha um otimo dia')