#Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros menores do que 100.
#Escolha números aleatórios entre 1 e 100, e mostre na tela a pergunta:
#Qual é a soma de a+b onde a e b são números aleatórios.
#Peça a resposta.
#Faça 5 perguntas ao aluno, e mostre para ele as perguntas e as respostas corretas, além de quantas vezes o aluno acertou.
from random import randint

c = 0
for contador in range(1, 6):
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    conta = int(input(f'{contador}- Qual o valor da soma de {num1} + {num2}? ='))
    resul = num1 + num2
    if conta == resul:
        print('Acertou miserável.')
        c += 1
    else:
        print('Erroouu.')
print(f'Você acertou {c} questões.')
