from datetime import date
dados = {}
pessoa = {}
da = date.today()
ano = da.year
#dados
dados['nome'] = input('Digite seu nome: ')
dados['data'] = int(input('Digite sua data de nascimento: '))
dados['carteira'] = int(input('Digite a carteira de trabalho (0 não tem): '))
#pessoa
pessoa['nome'] = dados['nome']
pessoa['idade'] = ano - dados['data']
pessoa['ctps'] = dados['carteira']
c = 0
if dados['carteira'] > 0:
    dados['adc'] = int(input('Digite o ano de contratação: '))
    dados['salario'] = int(input('Digite seu salario: '))
    pessoa['ano de contratação'] = dados['adc']
    pessoa['salario'] = dados['salario']
    c = ano - pessoa['ano de contratação']
    c = 35 - c
    c = pessoa['idade'] + c
    pessoa['data de aposento'] = c
print(pessoa)

for i, c in pessoa.items():
    print(f'o {i} tem o valor de {c}')