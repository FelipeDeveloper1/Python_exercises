from time import sleep
def fatorial(num, show='false'):
    """

    :param num:
    :param show (opcional), mostra o trajeto completo do fatorial do numero solicitado:
    :return: Retorna o fatorial do numero desejado
    """
    i = 1
    for c in range(num, 0, -1):
        i *= c
    if show == 'true':
        co = num
        while co != 1:
            print(f'{co} x', end=' ')
            co -= 1
        print(f'{co} ', end='')
        print(f'= {i}', end='')

    if show == 'false':
        print(i)


fatorial(5, show='true')
