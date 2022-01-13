from random import choice
print ('Muito bem, professor, digite o nome dos seus alunos para que eu sortie um')
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
print('Dessa sequência eu escolho {} para apagar o quadro.'.format(choice([n1, n2, n3, n4])))