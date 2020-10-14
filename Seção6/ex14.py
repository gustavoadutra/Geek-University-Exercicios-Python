#Faça um programa que leia um número inteiro postivo par N  e imprima todos os números pares de 0 até N em ordem crescente.
num = int(input('Número:'))
c = 0 
if num % 2 == 0:
    while num > c:
        c += 1
        if c % 2 == 0:
            print(c)