#Faça um programa que calcule e mostre a área de um trapézio.
#Lembra-se a base maior e a base menor devem ser números maiores que zero.
basemaior = int(input('Base Maior:'))
basemenor = int(input('Base Menor:'))
altura = int(input('Altura:'))
area = ((basemaior + basemenor) * altura) / 2
print(area)