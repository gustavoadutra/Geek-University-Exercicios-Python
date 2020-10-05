#Faça um programa que leia um número e, caso seja positivo, calcule e mostre:
    #O número digitado ao quadrado.
    #A raiz quadrada do número.
num = float(input('Número:'))
if num % 2 == 0:
    quad = num ** 2
    raiz = num ** 0.5
    print(quad, raiz)