#Um produto vai sofrer aumento de acordo com a tabela.
#Leia o preço antigo, calcule e escreva o preço novo, escrevendo em seguida um mensagem em função do preço novo.
preço_ant = float(input('Preço Antigo:R$'))
if preço_ant < 50:
    preço_fin = preço_ant + (preço_ant * 0.05)
elif preço_ant < 100:
    preço_fin = preço_ant + (preço_ant * 0.1)
else:
    preço_fin = preço_ant + (preço_ant * 0.15)

if preço_fin < 80:
    print('Barato.')
elif preço_fin < 120:
    print('Normal.')
elif preço_fin < 200:
    print('Caro.') 
else:
    print('Muito Caro.')