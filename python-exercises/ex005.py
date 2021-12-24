nome = input('Olá, como posso te chamar? ')
n = int(input('Muito bem, {}, poderia me dizer um número: '.format(nome)))
n1 = (n - 1)
n2 = (n + 1)
print('O antecesor de {} é {}'.format(n, n1))
print('O sucessor de {} é {}'.format(n, n2))

