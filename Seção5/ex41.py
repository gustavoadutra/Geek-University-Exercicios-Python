#Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo com a tabela abaixo.
altura = float(input('Altura:'))
peso = int(input('Peso:'))
imc = peso / altura ** 2
if imc <= 18.5:
    print('Abaixo do Peso.')
elif imc <= 24.9:
    print('Saudável.')
elif imc <= 29.9:
    print('Peso em exesso.')
elif imc <= 34.9:
    print('Obesidade Grau 1.')
elif imc <= 39.9:
    print('Obesidade Grau 2(severa).')
elif imc > 40:
    print('Obesidade Grau 3(mórbida).')