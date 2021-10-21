distancia = int(input('Digite a distancia de sua viagem: '))
if distancia <= 200:
    preco = distancia * 0.50
    print(preco)
else:
    preco = distancia * 0.40
    print(preco)
