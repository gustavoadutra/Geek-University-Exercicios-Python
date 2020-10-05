#Três amigos jogaram na loteria. 
# Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada deu para a realização da aposta. 
# Faça um programa que leia quanto cada apostador investiu, valor do prêmio, e imprima quanto cada um ganharia do prÊmio com base no valor investido.
valor = float(input('Valor do prêmio: R$'))
apos1 = float(input('1- Apostador: R$'))
apos2 = float(input('2- Apostador: R$'))
apos3 = float(input('3- Apostador: R$'))
#Cálculos:
#Somando o valor para calcular o valor da aposta total e em seguida a porcentagem que cada um ajudou para o prêmio final.
valor_apos = apos1 + apos2 + apos3
apos1_porc = apos1 / valor_apos
apos2_porc = apos2 / valor_apos
apos3_porc = apos3 / valor_apos
#Printando o resultado:
print(f'O apostador 1 ganhará: R${(apos1_porc * valor):.2f}\nO apostador 2 ganhará: R${(apos2_porc * valor):.2f}\nO apostador 3 ganhará: R${(apos3_porc * valor):.2f}')