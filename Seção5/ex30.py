#Faça um programa que receba três números e mostre-os em ordem crescente.
num1 = int(input('Valor 1:'))
num2 = int(input('Valor 2:'))
num3 = int(input('Valor 3:'))
if num3 > num1 < num3:
    print(num1)
    if num2 < num3:
        print(num2)
        print(num3)
    elif num3 < num2:
        print(num3)
        print(num2)

if num1 > num2 < num3:
    print(num2)
    if num1 < num3:
        print(num1)
        print(num3)
    elif num3 < num1:
        print(num3)
        print(num1)

if num1 > num3 < num2:
    print(num3)
    if num1 < num2:
        print(num1)
        print(num2)
    elif num2 < num1:
        print(num2)
        print(num1)