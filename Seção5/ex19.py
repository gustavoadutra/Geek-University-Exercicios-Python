#Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou 5, mas não simultaneamente pelos dois.
num = int(input('Número:'))
if num % 3 == 0 and num % 5 == 0:
    print('Ele é divisível pelos dois.')
elif num % 3 == 0 or num % 5 == 0:
    print('Ok')
else:
    print('GOL')