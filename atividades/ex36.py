valordacasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor de seu salario: '))
anos = int(input('Digite em quantos anos irá financiar o imovel: '))
# calculando #
meses = 12 * anos
mensalidade = valordacasa / meses
#fazendo a condição do calculo
if mensalidade < salario * 30 / 100:
    print('\033[32m Você teve sucesso em seu financialmento \033[m')
    print('Quantidade de meses será {} e a mensalidade será {:.3f}'.format(meses, mensalidade))
else:
    print('\033[31m Quantidade de meses será {} e a mensalidade será {:.3f}'.format(meses, mensalidade))
    print('Infelizmente não sera possivel o financeamento dessa casa \033[m ')
    print('temos outras casas que podem ser compativeis ao seu financiamento')
