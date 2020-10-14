#Escreva um prograa que declare um inteiro, inicialize-o, incremente-o de 1000 em 1000,
#imprimindo seu valor na tela, até que seu valor seja 100000.
num = int(input('Número:'))
while num < 100000:
    num += 1000
    print(num)