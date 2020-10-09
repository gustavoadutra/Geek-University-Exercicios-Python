#Escreva um programa que, dada a idade de um nadador e classifique ele conforme as categorias.
idade = int(input('Idade:'))
if 5 <= idade <= 7:
    print('Infantil A.')
elif 8 <= idade <= 10:
    print('Infantil B.')
elif 11 <= idade <= 13:
    print('Juvenil A.')
elif 14 <= idade <= 17:
    print('Juvenil B.')
elif 18 <= idade:
    print('Sênior.')