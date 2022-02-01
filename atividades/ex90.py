dados = {}
dados['nome'] = input('Digite seu nome: ')
dados['media'] = int(input(f'Digite sua media, {dados["nome"]}: '))
print(f'Seu nome é {dados["nome"]}')
print(f'Media é igual a {dados["media"]}')
if dados["media"] >= 5:
    print(f'Parabéns {dados["nome"]}, você foi APROVADO')
else:
    print(f'Infelizmente você foi REPROVADO')
