from math import trunc
nome = input ('Olá, como posso lhe chamar? ')
n = float(input('Muito bem, {}, poderia me dizer um número real: '.format(nome)))
print('A porção inteira de {} é {}'.format(n, trunc(n)))
