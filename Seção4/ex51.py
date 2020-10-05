#Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule sua distância da origem (0.0).
# y = ax + b

#Declarando variáveis:
lista_b = []
#Pegando os valores:
y = float(input('Valor de Y: '))
x = float(input('Valor de X: '))

#Começando tentando descobrir o valor de B:
a = (y / x) - 1
b = (x / y) - a
print(a, b)
