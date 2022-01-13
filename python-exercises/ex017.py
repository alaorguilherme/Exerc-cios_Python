from math import hypot
nome = input('Boas vindas, poderia me informar seu nome: ')
co = float(input('{}, poderia me dizer o comprimento cateto oposto do triângulo retângulo: '.format(nome)))
ca = float(input('e qual seria o do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa de {} e {} é igual a {:.2f}, muito obrigado.'.format(co, ca, hi))
