#Faça um programa que leia três números inteiros positivos e efetue o 
# cálculo de uma das seguintes médias de acordo com um valor numérico digitado pelo usuário.
print('         Média')
print(' (a) Geometria\n (b) Ponderada\n (c) Harmônica\n (d) Aritmética')
escolha = str(input('Escolha:')).lower()
num1 = int(input('Valor x:'))
num2 = int(input('Valor y:'))
num3 = int(input('Valor z:'))
if escolha == 'a':
    r = (num1 * num2 * num3) ** (1/3)
    print(f'A média geométrica é {r}')
if escolha == 'b':
    r = (num1 + 2 * num2 + 3 * num3) / 6
    print(f'A média ponderada é {r}')
if escolha == 'c':
    r = 1 / 1 / num1 + num2 + num3
    print(f'A média harmônica é {r}')
if escolha == 'd':
    r = (num1 + num2 + num3) / 3
    print(f'A média aritmética é {r}')