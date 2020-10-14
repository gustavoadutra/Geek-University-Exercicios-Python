#Faça um programa que leia um número inteiro postivo ímpar N  e imprima todos os números ímpares de 0 até N em ordem crescente.
num = int(input('Número:'))
if num % 2 != 0:
    while num > 0:
        num -= 1
        if num % 2 != 0:
            print(num)