from time import sleep
def maior(*num):
    m = max(num)
    me = min(num)
    print(f'Há {len(num)} numeros')
    print(f'{num}: o maior numero é {m} e o menor é {me}')
    sleep(1)
    print()


maior(3, 5 ,18, 11, 6, 7, 9,1 )

maior(2,5,10,9)

maior(5,9,8,10,3)

maior(9,7,6,1,3)