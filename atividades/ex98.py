from time import sleep

for c in range(1, 11, 1):
    print(f'{c} ', end='', flush= True)
    sleep(0.5)
print()
for b in range(10, -2, -2):
    print(f'{b} ', end='', flush=True)
    sleep(0.5)
print()
print('personalize a contagem')

def contador(inicio, fim, passo):

    if fim > inicio:
        if passo == 0:
            passo += 1
        for a in range(inicio, fim+1, passo):
            print(f'{a} ', end=' ', flush= True)
            sleep(0.5)
    if fim < inicio:
        for a in range(inicio, fim-1, -passo):
            print(f'{a} ', end=' ', flush=True)
            sleep(0.5)
    if passo <= -1:
        for a in range(inicio, fim, passo):
            print(f'{a} ', end=' ', flush= True)
            sleep(0.5)


inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))

contador(inicio, fim, passo)