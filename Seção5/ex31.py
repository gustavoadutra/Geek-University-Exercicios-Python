# Faça um programa que receba a altura e o peso de uma pessoa.
# De acordo com a tabela a seguir, verifique e mostre qual a classificação dessa pessoa.
alt = float(input('Altura:'))
peso = int(input('Peso:'))

if peso <= 60:
    if alt <= 1.2:
        print('A')
    elif alt <= 1.7:
        print('B')
    elif alt > 1.7:
        print('C')
elif peso <= 90:
    if alt <= 1.2:
        print('D')
    elif alt <= 1.7:
        print('E')
    elif alt > 1.7:
        print('F')
else:
    if alt <= 1.2:
        print('G')
    elif alt <= 1.7:
        print('H')
    elif alt > 1.7:
        print('I')