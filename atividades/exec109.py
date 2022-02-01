import ex108
from ex109 import dobro, aumentar, reduzir, metade
p = int(input('Digite um valor: '))
print(f'O dobro de {ex108.moeda(p)} é {dobro(p, True)}')
print(f'A metade de {ex108.moeda(p)} é {metade(p, True)}')
print(f'O aumento de 20% é {aumentar(p, 20, True)}')
print(f'A redução de 10% é {reduzir(p, 10, True)}')
