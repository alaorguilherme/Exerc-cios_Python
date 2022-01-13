import math
nome = input('Boas vindas, como posso lhe chamar? ')
â = float(input('{}, poderia me dizer o ângulo que iremos destrinchar hoje: '.format(nome)))
â2 = math.radians(â)
print('Baseado no ângulo {} posso dizer que o seno é {:.2f}, cosseno {:.2f} e a tangente {:.2f}.'.format(â, math.sin(â2), math.cos(â2), math.tan(â2)))