#Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número, com exceção dele próprio.
num = int(input('Valor:'))
soma = 0

for n in range(1, num):
    if num % n == 0:
        soma += n

print(soma)