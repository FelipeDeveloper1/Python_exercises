import ex108
n1 = int(input('Digite um valor: R$: '))
print(f'A metade de {ex108.moeda(n1)} é {ex108.moeda(ex108.metade(n1))}')
print(f'O dobro de {ex108.moeda(n1)} é {ex108.moeda(ex108.dobro(n1))}')
print(f'O aumento de 10% é {ex108.moeda(ex108.aumentar(n1,10))}')
print(f'A redução de 10% é {ex108.moeda(ex108.diminuir(n1, 10))}')