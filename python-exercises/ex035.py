nome = str(input('Olá, poderia digitar seu nome: '))
r1 = float(input('{}, poderia me dizer o comprimento de três retas: '.format(nome)))
r2 = float(input())
r3 = float(input())
if r1+r2 > r3 and r1 + r3 > r2 and r2+r3 > r1:
    print('Com essas medidas podemos formar um triângulo.')
else:
    print('Não é possível formar um triângulo com essas medidas, sinto muito.')
