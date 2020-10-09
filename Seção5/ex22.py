#Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não pode se aposentar.
#Levando em conta as condições de aposentadoria.
idade = int(input('Idade:'))
tempo = int(input('Tempo de serviço:'))
if idade >= 65 or tempo >= 30 or idade >= 60 and tempo >= 25:
    print('Pode se aposentar.')
else:
    print('Não pode se aposentar.')