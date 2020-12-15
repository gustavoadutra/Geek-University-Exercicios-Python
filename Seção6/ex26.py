#Faça um programa que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado.
num = int(input('Valor:'))
for n in range(1, num + 1):
    if n % 11 == 0 or n % 13 == 0 or n % 15 == 0:
        print(n)
        break


        