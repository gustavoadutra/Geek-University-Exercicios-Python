#Leia a nota e o número de faltas de um aluno, e escreva seu conceito.
#De acordo com a tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma redução de conceito.
nota = float(input('Nota:'))
falt = int(input('Faltas:'))

if 9 <= nota <= 10:
    if falt >= 20:
        print('A')
    else:
        print('B')
if 7.5 <= nota <= 8.9:
    if falt >= 20:
        print('B')
    else:
        print('C')
if 5 <= nota <= 7.4:
    if falt >= 20:
        print('C')
    else:
        print('D')
if 4 <= nota <= 4.9:
    if falt >= 20:
        print('D')
    else:
        print('E')
if 0 <= nota <= 3.9:
    if falt >= 20:
        print('E')
    else:
        print('E')