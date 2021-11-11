palavras = ('ola', 'dia bom', 'hi', 'buy', 'python', 'nicee', 'dev')
for palavra in palavras:
    print(f'\n Na palavra {palavra} temos: ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(f'{letra}', end=' ')