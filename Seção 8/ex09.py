#Faça uma funções que receba a altura e o raio de um cilindro circular e retorne o volume do cilindro;

def cilindro(h, pi=3.14, r):
    area = h * pi * r ** 2
    return area

print(cilindro(2, 3.14, 3))