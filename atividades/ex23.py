n1 = float(input('Digite um numero de 0 a 9999: '))
unidade = n1 // 1 % 10
dezenas = n1 // 10 % 10
centena = n1 // 100 % 10
milhar = n1 // 1000 % 10
print('A unidade: é {}, dezenas: é {}, centena: {}, milhar: {}'.format(unidade, dezenas, centena, milhar))