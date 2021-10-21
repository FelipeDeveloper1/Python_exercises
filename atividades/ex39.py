idade = int(input('Digite sua idade: '))
## mini calculo
idade_restante = 18 - idade
idade_ultrapassada = idade - 18
if idade < 18:
    print(f'falta {idade_restante} ano(s) para você se alistar')
elif idade > 18:
    print(f'\033[31m Já fez seu alistamento? se não, você está {idade_ultrapassada} ano(s) atrasado \033[m ')
elif idade == 18:
    print(f'Chegou sua hora de se alistar no exercito brasileiro ')
print('Tenha um otimo dia')