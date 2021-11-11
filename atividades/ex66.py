c = n = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    c += n
print(f'A soma de tudo foi {c}')