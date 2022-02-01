lista = []
for a in range(0, 5):
    num = int(input('Digite um numero: '))
    if a == 0 or num > lista[-1]:
        lista.insert(4, num)
        print('Adicionado na ultima posição')
    else:
        c = 0
        while c < len(lista):
            if num <= lista[c]:
                lista.insert(c, num)
                print(f'Adicionado na {c} posição ')
                break
            c += 1
print(lista)