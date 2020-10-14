#Fala um programa que leia um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem.
c = 0
num = int(input('Número:'))
if num % 2 == 0:
    while num > c:
        c += 1
        print(c)
    