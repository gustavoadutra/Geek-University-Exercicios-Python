#Faça um programa que leia um número inteiro positivo n e calcule a soma dos n primeiros números.
num = int(input('Números:'))
soma = num
for c in range(num, num + 4):
    soma += num
print(soma)