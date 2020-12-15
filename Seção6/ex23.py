#Faça um programa que leia um número positivo e imprima os divisores.
valor = int(input('Valor:'))
if valor % 2 == 0:
    for c in range(1, valor):
        if valor % c == 0:
            print(f'{c},', end=' ')
print('PAH')
