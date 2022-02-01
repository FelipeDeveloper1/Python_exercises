from datetime import date
hoje = date.today()
ano = hoje.year
print(ano)
def voto(idade):
    if ano - idade < 16:
        print(f'Com {ano - idade} anos, Não vota')
    elif 16 <= ano - idade < 18 or ano - idade > 65:
        print('Voto opcional')
    elif ano - idade >= 18:
        if ano - idade < 60:
            print(f'Com {ano - idade} anos, Voto obrigatorio')





idade = int(input('Em que ano você nasceu: '))
voto(idade)
