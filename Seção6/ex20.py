#Ler uma sequência de números inteiros e determinar se eles são pares ou não.
#Deverá ser informado o número de dados lidos e número de valores pares.
#O processo termina quando for digitado o número 1000.
cont = pares = 0
while True:
    num = int(input('Número:'))
    cont += 1
    if num % 2 == 0:
        pares += 1
    if num == 1000:
        break
print(cont, pares)
    