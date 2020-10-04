#Leia um número inteiro de 4 dígitos e imprima 1 digito por linha.
num = int(input('Número:'))
print(str(int(num // 1000))[-1])
print(str(int(num/100))[-1])
print(str(int(num/10))[-1])
print(str(int(num/1))[-1])