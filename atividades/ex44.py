produto_valor = float(input('Digite o valor do produto: '))
formadepagamento = input('Digite a forma de pagamento: ').capitalize()
vezes = int(input('se for no cartão, digite a quantidade de vezes, caso contrario, digite 0: '))
dc = produto_valor - produto_valor * 5 / 100
dd = produto_valor - produto_valor * 10 / 100
juros = produto_valor + produto_valor * 20 / 100

if formadepagamento == 'Cartão' and vezes == 1:
   print(f'seu produto a vista no cartão fica {dc}R$')
elif formadepagamento == 'Cartão' and vezes == 2:
    print(f'Seu produto em 2x no cartão fica o preço sem desconto, {produto_valor}R$')
elif formadepagamento == 'Cartão' and vezes == 3:
    print(f'Quantidade de parcela em 3x terá o acréscimo de {juros}R$')
elif formadepagamento == 'Cartão' and vezes <= 4:
    print('Quantidade de vezes invalida')
elif formadepagamento == 'Dinheiro':
    print(f'Você adquiriu desconto, o valor é {dd}')
