import ex109
import ex108
def dados(p, a = 0, r = 0 ):
    print('-'*30)
    print('  RESUMO DO VALOR')
    print('-'*30)
    print(f'Preço analisado:    \t{ex108.moeda(p)}')
    print(f'preço em dobro:     \t{ex109.dobro(p, True)}')
    print(f'Metade do preço:    \t{ex109.metade(p, True)}')
    print(f'{a}% de aumento é:   \t{ex109.aumentar(p, a, True)}')
    print(f'{r}% de redução é:   \t{ex109.reduzir(p, r, True)}')



