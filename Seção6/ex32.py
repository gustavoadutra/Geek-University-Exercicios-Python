#Faça um programa que simula o lançamento de dois dados, d1 e d2, n vezesm e tem como saída o número de cada daod e a relação entre eles de cada lançamento.
from random import randint

dado1 = randint(0,8)
dado2 = randint(0,8)

if dado1 == dado2:
    print('Os dois são iguais.')
elif dado1 > dado2:
    print('O dado 1 é maior.')
    for c in range(dado2, dado1):
        print(c, end=', ')
elif dado2 > dado1:
    print('O dado 2 é maior.')
    for c in range(dado1, dado2):
        print(c, end=' ')
print('\nSão os valores que ficam no meio do mesmo.')
