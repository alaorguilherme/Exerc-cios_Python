from random import choices, shuffle
print('Boa tarde, professor, digite o nome dos integrantes do grupo do trabalho')
a1 = str(input('Integrante um: '))
a2 = str(input('Integrante dois: '))
a3 = str(input('Integrante três: '))
a4 = str(input('Integrante quatro: '))
g = [a1, a2, a3, a4]
shuffle(g)
print('A ordem de apresentação será: {}'.format(g))

