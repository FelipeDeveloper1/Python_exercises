n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
maior = 0
escolha = int(input('Digite o que deseja, '
                    '\n [1] somar '
                    '\n [2] multiplicar'
                    '\n [3] maior numero'
                    '\n [4] novos numeros'
                    '\n [5] finalizar tarefa: '))
while escolha > 5 or escolha < 1:
    print('Opção invalida')
    escolha = int(input('Digite o que deseja: '
                        '\n [1] somar'
                        '\n [2] multiplicar'
                        '\n [3] maior numero'
                        '\n [4] novos numeros'
                        '\n [5] finalizar tarefa: '))
if escolha == 4:
    n1 = int(input('Digite o primeiro numeros: '))
    n2 = int(input('Digite o segundo numero: '))
    escolha = int(input('Digite o que deseja: '
                        '\n [1] somar'
                        '\n [2] multiplicar'
                        '\n [3] maior numero'
                        '\n [4] novos numeros'
                        '\n [5] finalizar tarefa: '))
if escolha == 1:
    print(f'A soma é: {n1 + n2}')
elif escolha == 2:
    print(f'A multiplicação é: {n1 * n2}')
elif escolha == 3:
    maior = n1
    if n2 > n1:
        maior = n2
    print(f'O maior é {maior}')
elif escolha == 5:
    print('Tenha um otimo dia')
    print('Fim')
