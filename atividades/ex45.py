import random
decisao = ['Pedra', 'Papel', 'Tesoura']
jogada = input('Escolha entre pedra papel e tesoura: ').capitalize()
escolha = random.choice(decisao)
print(escolha)
# jogador vencendo
if jogada == 'Pedra' and escolha == 'Tesoura':
    print('Você ganhou :( ')
elif jogada == 'Tesoura' and escolha == 'Papel':
    print('Você ganhou :( ')
elif jogada == 'Papel' and escolha == 'Pedra':
    print('Você ganhou :( ')
# eu ganho
elif escolha == 'Tesoura' and jogada == 'Papel':
    print('EU VENCI :) ')
elif escolha == 'Pedra' and jogada =='Tesoura':
    print('Eu venci :) ')
elif escolha == 'Papel' and jogada == 'Pedra':
    print('Eu venci :] ')
# empate
elif escolha == jogada:
    print('Empate que se fala, ne? ')
else:
    'Jogada invalida'