nun = [[], []]
val = 0
for c in range(0, 8):
    val = int(input('Digite um numero: '))
    if val % 2 == 0:
        num[0].append(val)
    else:
        num[1].append(val)