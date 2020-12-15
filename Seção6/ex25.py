#Faça um programa que some todos os números naturais abaixao de 1000 que são múltiplos de 3 ou 5;
soma = 0

for nums in range(0, 1000):
    if nums % 3 == 0 or nums % 5 == 0:
        soma += nums

print(soma)