#Faça uma função para verificar se o número é um quadrado perfeito.
def quadrado_perfeito(num):
    if num ** (1/2) == 0:
        print('Quadrado Perfeito.')
    else:
        print('Não é um quadrado perfeito.')

quadrado_perfeito(16)