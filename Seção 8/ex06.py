#Faça uma função que receba 3 números inteiros como parâmetro, representando horas minutos e segundos, e os converta em segundos.


def seconds(seg, min, hor):
    tot = seg + min * 60 + hor * 60 * 60
    return tot 


print(seconds(10, 30, 2))