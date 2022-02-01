dados = list()
pessoa = list()
media = list()
while True:
    dados.append(input('Digite seu nome: '))
    dados.append(input('Digite a 1° nota: '))
    dados.append(input('Digite a 2° nota: '))
    pessoa.append(dados[:])
    dados.clear()
    c = input('Deseja continuar: ').upper()
    if c in 'NAO NOP NA NAH NAUM NO NÃO':
        break
for c, i in enumerate(pessoa):
    cal = (int(i[1]) + int(i[2])) / 2
    media.append(cal)
    #print(f'{c}    {i[0]}    {media[c]}')
    print(f'{c} ', end='     ')
    print(f'{i[0]}', end='      ')
    print(f'{media[c]}')
nota = int(input('Deseja ver a nota de qual aluno?  (999 interrompe): '))
while True:
    if nota != 999:
        print(f'você escolheu as notas de {pessoa[nota][0]} e as notas foram: {pessoa[nota][1]}, {pessoa[nota][2]} ')
        nota = int(input('Deseja ver a nota de qual aluno?  (999 interrompe): '))
    if nota == 999:
        print('obrigado')
        break


