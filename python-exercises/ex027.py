n = str(input('Olá, poderia digitar seu nome completo: ')).strip().split()
print('Seu primeiro nome é {}, e seu último nome é {}. É um prazer te conhecer, {}.'.format(n[0], n[len(n)-1], n[0]))
