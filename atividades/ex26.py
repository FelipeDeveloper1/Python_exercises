frase = input('Digite uma frase inteira: ').lower().strip()
quantosA = frase.count('a')
primeiroA = frase.find('a')+1
ultimoA = frase.rfind('a')
print(primeiroA)
print(quantosA)
print(ultimoA)
