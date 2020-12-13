#Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles quantas vezes maior foi lido.
#A quantidade de números a serem lidos deve ser fornecido pelo usuário.
cont = maior = 0
n = int(input('Quantidade números a serem digitados:'))
for c in range(0, n):  
    num = int(input("Número:"))
    if num > maior:
        cont = 0
        maior = num
    if num == maior:
        cont += 1
print(cont, maior)