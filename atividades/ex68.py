import random
n2 = random.randint(1, 10)
escolha = ''
n1 = quanti = 0
while True:
    escolha = str(input('Escolha, impar ou par: ')).capitalize()
    n1 = int(input('Escolha um numero de 0 a 10: '))
    n2 = random.randint(1, 10)
    soma = n1 + n2
    if escolha == 'Par' and soma % 2 == 0:
        print(f'VOCÊ GANHOU, {soma}')
        quanti += 1
    elif escolha == 'par' and soma % 2 == 0:
        print(f'Você perdeu, {soma}')
        print(f'Total de vitorias {quanti}')
        break
    else:
        if escolha == 'Impar' and soma % 2 == 1:
            print(f'VOCÊ GANHOU {soma}')
            quanti += 1
        elif escolha == 'Impar' and soma % 2 == 0:
            print(f'Você perdeu, {soma}')
            print(f'Total de vitorias {quanti}')
            break





