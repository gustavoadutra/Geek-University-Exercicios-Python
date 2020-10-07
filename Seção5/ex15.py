#Usando switch, escreva um programa que leia um número inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número.
#Isto é, domingo se 1, segunda feira se 2, e assim por diante.
num = int(input('Número:'))
if num == 1:
    print('Domingo.')
elif num == 2:
    print('Segunda.')
elif num == 3:
    print('Terça.')
elif num == 4:
    print('Quarta.')
elif num == 5:
    print('Quinta.')
elif num == 6:
    print('Sexta.')
elif num == 7:
    print('Sábado.')