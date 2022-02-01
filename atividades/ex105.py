def nota(*notas, situ = False):
    dados = {}
    dados['total'] = len(notas)
    dados['maior'] = max(notas)
    dados['menor'] = min(notas)
    dados['media'] = sum(notas) / len(notas)
    if situ == True:
        if dados['media'] >= 6:
            dados['situação'] = 'Boa'
        if dados['media'] <= 5:
            dados['situação'] = 'Ruim'

    return dados



a = nota(10, 10, 9, 10, situ=False)
print(a)