c = str(input('Olá, pessoa, poderia me dizer o nome de uma cidade: ')).strip()
c1 = c.capitalize()
p = c1.startswith('Santo')
print('A cidade {} começa com a palavra Santo: {}.'.format(c, p))