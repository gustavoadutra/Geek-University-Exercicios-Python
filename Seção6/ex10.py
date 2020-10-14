#Faça um programa que calcule e mostre a soma dos 50 primeiros pares.
pares = num = 0
continua = True
while continua:
    if pares == 50:
        continua = False
    else:
        if num % 2 == 0:
            print(num)
            pares += 1
    num += 1
    
