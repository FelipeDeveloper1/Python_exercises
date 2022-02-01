from utilidades import dado
from utilidades import moeda
dado.dados(3000, 10, 10)

n = int(input('Digite um numero: '))
print(moeda.dobro(n, True))
print(moeda.metade(n, True))
print(moeda.reduzir(n, 10, True))
print(moeda.aumentar(n, 20, True))