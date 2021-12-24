nome = input('Olá, como posso te chamar? ')
n = int(input('Tudo bem, {}? Poderia me dizer um número: '.format(nome)))
n1 = (n*2)
n2 = (n*3)
n3 = (n**(1/2))
print('{}, eu posso te dizer que o dobro de {} é {}, seu triplo é igual a {} e sua raiz quadrada é {:.3}'
      .format(nome, n, n1, n2, n3))
