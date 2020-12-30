#Faça um programa que calcule o menor número divisível por cada um dos números de 1 a 20.
cont = cer = 0
while True:
    cer = 0
    cont += 1 # Vai fazer os números correrem.

    for num in range(10, 21):# Vai fazer a verificação de cada número.
        if cont % num == 0:# Se o contador divisível:
            cer += 1
        if cer == 10:
            print(num)
            break
    if cer == 10:
        break