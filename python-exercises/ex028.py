import random as rd
nome = str(input('Olá, pessoa, poderia digitar seu nome: '))
n = rd.choice([0, 1, 2, 3, 4, 5])
print('Muito bem, {}, eu escolhi um número de 0 a 5, gostaria de tentar adivinhá-lo? '.format(nome))
n2 = int(input('Qual número eu escolhi: '))
if n2 == n:
    print('Muito bem, você acertou!')
else:
    print('Infelizmente você errou, mais sorte na próxima :)')
