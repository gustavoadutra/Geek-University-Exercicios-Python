# Faça um programa utilizando o comando while que mostra uma contagem regressiva na tela, iniciando em 10 e terminando em 0.
# Mostrar uma mensagem "FIM!" após a contagem.
continua = True
num = 10
while continua:
    print(num)
    if num == 0:
        continua = False
    num -= 1
print("FIM!")