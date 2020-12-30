#Faça um programa que calcule e escreva o valor de S:

c = s = 0

for x in range(1, 100, 2):
    c += 1
    s += x / c

print(s)