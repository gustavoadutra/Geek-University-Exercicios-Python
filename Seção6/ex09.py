#Faça um programa que leia um número inteiro N e depois imprima  os N primeiros números naturais ímpares.
n = int(input('Número:'))
for num in range(n, n + 10):
    n += 1
    if n % 2 == 0:
        print(n)