n1 = int(input('Digite o numero inicial: '))
razao = int(input('Digite sua razão: '))
contador = 10
while contador != 0:
    n1 += razao
    print(n1)
    contador -= 1
termos = int(input('Se Você deseja adicionar mais termos, informe o numero, caso contrario, digite 0: '))
contador += termos
while termos > 0:
    while contador > 0:
        n1 += razao
        print(n1)
        contador -= 1
    termos = int(input('Se Você deseja adicionar mais termos, informe o numero, caso contrario, digite 0: '))
    contador += termos
if termos == 0 or termos < 0:
    print('Fim do programa')