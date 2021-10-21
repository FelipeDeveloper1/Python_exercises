import math
catetooposto = int(input('Digite o valor do cateto oposto: '))
catetoadj = int(input('Digite o valor do cateto Adjacente: '))
elev1 = catetooposto**2
elev2 = pow(catetoadj, 2)
hipotenusa = elev2 + elev1
print('A hipotenusa é {}'.format(hipotenusa))
