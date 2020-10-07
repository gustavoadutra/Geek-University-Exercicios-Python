#Dados três valores, verificar se eles podem ser valores dos lados de um triângulo e, se forem, se é um triângulo equilátero, escaleno ou isóceles.
a = int(input('Valor de A:'))
b = int(input('Valor de B:'))
c = int(input('Valor de C:'))

if a == b == c:
    print('O triângulo é equilátero.')
elif a == b != c or a != b == c or a == c != b:
    print('O triângulo é isóceles.')
else:
    print('O triângulo é escaleno.')