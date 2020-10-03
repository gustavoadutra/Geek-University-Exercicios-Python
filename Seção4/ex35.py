#Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação: h² = a² + b². Faça um programa que receba os valores de a e b e calcule o valor de h através da equação. Por fim imprimindo o resultado da operação.
a = float(input('a = '))
b = float(input('b = '))
h = ((a ** 2) + (b ** 2)) ** 1/2
print(h)