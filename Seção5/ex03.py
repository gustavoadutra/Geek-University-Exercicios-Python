# Leia um número real. 
# Se o número for positivo imprima a raiz quadrada.
# Do contrário, imprima o número ao quadrado.
num = float(input('Número:'))
if num % 2 == 0:
    print(num ** 0.5)
else:
    print(num ** 2)