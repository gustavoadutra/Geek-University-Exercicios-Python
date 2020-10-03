#A importância de R$ 780.000,00 será dividida entre os três ganhadores do concurso. Sendo que o primeiro receberá 46%, o segundo 32% e o terceiro o restante.
#Calcule e imprima a quantia ganha por cada um dos ganhadores.
tot = 780000
pri = tot * 0.46
seg = tot * 0.32
ter = tot - (pri + seg) 
print(f'O primeiro recebeu R${pri:.2f}, o segundo R${seg:.2f} e o terceiro ficou com R${ter:.2f}.')