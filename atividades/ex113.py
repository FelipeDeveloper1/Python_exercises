a = b = div = 0
def leiaint(msn = 'digite um valor: '):
    global a, b, div
    while True:
            try:
                a = int(input(msn))
                return a
            except ValueError:
                print('\033[31m Erro, digite um valor inteiro valido \033[m')
                continue
            except KeyboardInterrupt:
                print('O usuario preferiu não digitar um valor')
                a += 0
                return a
                break
            else:
                break

def leiafloat(msn1 = 'digite um valor real: '):
        global a, b, div
        while True:
                try:
                    b = float(input(msn1))
                    return b
                except ValueError:
                    print('\033[31m Digite um valor real valido \033[m')
                    continue
                except KeyboardInterrupt:
                    print('O usuario preferiu não digitar um valor')
                    b += 0
                    return b
                    break
                else:
                    break





n1 = leiaint('Digite um valor inteiro: ')
n2 = leiafloat('Digite um valor real: ')

print(f'O valor inteiro foi {n1} e o real foi {n2}')

