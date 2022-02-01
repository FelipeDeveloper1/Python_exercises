def ajuda():
    a = '\033[31m sistema de ajuda PyHelp'
    print('\033[31m~'*len(a))
    print(a)
    print('~'*len(a))
    while True:
        valor = input('Função ou biblioteca: ')
        b = f'Acessando o manual do comando "{valor}" '
        print(len(b)*'\033[32m~')
        print(b)
        print(len(b)*'\033[32m~')
        print(f'\033[36m{help(valor)}')
        if valor == 'fim':
            c = 'Ate logo'
            print(f'\033[38m{len(c)*"~"}')
            print(c)
            print(f'{len(c)*"~"}')
            break
ajuda()