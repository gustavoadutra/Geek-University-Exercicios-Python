#Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado, uma sequência arbitrária de notas e que mostre na tela, como resultado, a correspondente média aritmética.
soma = cont = 0
while True:
    nota = int(input('Nota:'))
    if not 10 < nota < 20:
        break
    cont += 1
    soma += nota
    
print(soma / cont)