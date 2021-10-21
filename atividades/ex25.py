nome = input('Digite seu nome: ').lower()
silva = nome.find('silva')
if silva != -1:
    print('Seu nome tem silva, que bonito')
print(f'Bem vindo, {nome}')