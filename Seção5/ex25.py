#Calcule as raízes da equação do segundo grau.
print('      INFORME OS VALORES:')
a = float(input('A:'))
while a == 0:
    print('"A" tem que ser diferente de zero.')
    a = float(input('A:'))
b = float(input('B:'))
c = float(input('C:'))
delta = b ** 2 - 4 * a * c
print(f'O valor de Delta é igual a {delta}.')
if delta < 0:
    print('Não existe raiz.')
elif delta == 0:
    x = - b / 2 * a
    print('Como o delta é 0.')
    print(f'O resultado é {x}.')
else:
    x1 = (-b + delta ** 0.5) / 2 * a
    x2 = (-b - delta ** 0.5) / 2 * a
    print(f'X1 = {x1}')
    print(f'X2 = {x2}')
