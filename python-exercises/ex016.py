nome = input('Olá, como posso lhe chamar? ')
n = float(input('Muito bem, {}, poderia me dizer um valor real: '.format(nome)))
print('Sendo o valor digitado {} sua porção inteira é {}.'.format(n, int(n)))