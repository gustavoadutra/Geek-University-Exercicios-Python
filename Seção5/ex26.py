#Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um percurso, calcule o consumo em Km/l e escreva uma mensagem.
km = float(input('Km:'))
l = float(input('Litros:'))
if km % l <= 8:
    print('Venda o carro!')
elif km % l > 8 and km % l <= 14:
    print('Econômico!')
elif km > 14:
    print('Super Econômico!')