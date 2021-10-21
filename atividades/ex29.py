velocidade = int(input('Digite a velocidade de seu carro: '))
vm = 80
if velocidade > vm:
    velultr = (velocidade - vm)
    multa = velultr * 7
    print(f"Sua velocidade foi {velocidade}, você foi multado em {multa} Reais")
else:
    print('Tenha um otimo dia')