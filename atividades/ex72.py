n10 = ('zero', 'um', 'dois', 'três', 'quatro','cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
n20 = ('onze', 'doze', 'treze','quatorze', 'quinze',  'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numbers = n10 + n20
num = int(input('Digite um numero de 0 a 20: '))
while True:
    if num > 20 or num < 0:
        print('Numero invalido')
        num = int(input('Digite um numero de 0 a 20: '))
    else:
        print(numbers[num])
        break
