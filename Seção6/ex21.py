#Faça um programa que receba dois números.
num1 = int(input('Valor:'))
num2 = int(input('Valor:'))
soma = 0
multi = 1
for c in range(num1, num2 + 1):
    if c % 2 == 0:
        soma += c
    else:
        multi *= c 

print(soma, multi)