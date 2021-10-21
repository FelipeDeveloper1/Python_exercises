n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print(f'\033[31m Infelizmente você foi reprovado. {media} \033[m')
elif media == 5.0 or media <= 6.9:
    print(f'\033[33m Você esta de recuperação. {media} \033[m ')
elif media == 7.0 or media <= 10:
    print(f'\033[32m você foi aprovado. {media} ')
elif media >= 11:
    print('Error, media invalida')
print('Tenha um otimo dia')