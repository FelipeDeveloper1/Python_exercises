n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
for i in range(1, 2):
    peso = int(input('Digite seu peso: '))
    n1 = + peso
    print(n1)
for i in range(1, 2):
    peso = int(input('Digite seu peso: '))
    n2 += peso
    print(n2)
for i in range(1, 2):
    peso = int(input('Digite seu peso: '))
    n3 += peso
    print(n3)
for a in range(1, 2):
    peso = int(input('Digite seu peso: '))
    n4 += peso
    print(n4)
for i in range(1, 2):
    peso = int(input('Digite seu peso: '))
    n5 += peso
#maior
maior = n1
if n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
    maior = n2
    print(f'O maior é {n2}')
elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
    print(f'O maior é {n3}')
elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
    print(f'O maior é {n4}')
elif n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
    print(f'O maior é {n5}')
elif n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
    print(f'O maior é {maior}')
#menor
menor = n1
if n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5:
    print(f'O menor é {n2}')
if n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5:
    print(f'O menor é {n3}')
if n4 < n1 and n4 < n2 and n4 < n3 and n4 < n5:
    print(f'O menor é {n4}')
if n5 < n1 and n5 < n2 and n5 < n3 and n5 < n4:
    print(f'O menor é {n5}')
elif n1 < n2 and n1 <n3 and n1 < n4 and n1 < n5:
    print(f'O menor é {menor}')