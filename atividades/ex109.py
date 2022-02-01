def dobro(num, show = False):
    num *= 2
    if show == True:
        return f'R${num}'
    else:
        return num

def metade(num, show=False):
    num /= 2
    if show == True:
        return f'R${num}'
    else:
        return num


def aumentar(num, p, show=False):
    c = num * p / 100
    num += c
    if show == True:
        return f'R${num}'
    else:
        return num

def reduzir(num, p, show=False):
    c = num * p / 100
    num -= c
    if show == True:
        return f'R${num}'
    else:
        return num