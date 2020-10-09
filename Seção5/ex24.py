#Uma empresa vende o mesmo produto para quatro diferentes estados.
#Cada estado possui uma taxa diferente.
#Faça um programa em que o usuário entre com o valor e o estado destino do produto e o programa retorne o preço final do produto acrecido do imposto do estado em que ele será vendido.
#Se o estado digitado não for válido, mostrar uma mensagem de erro.
val_prod = float(input('Valor do Produto:R$'))
estado = str(input('Estado:')).upper()
if estado == 'MG':
    print('R$', val_prod + val_prod * 0.07)
elif estado == 'SP':
    print('R$', val_prod + val_prod * 0.12)
elif estado == 'RJ':
    print('R$', val_prod + val_prod * 0.15)
elif estado == 'MS':
    print('R$', val_prod + val_prod * 0.08)
else:
    print('Por favor digite um estado válido.')