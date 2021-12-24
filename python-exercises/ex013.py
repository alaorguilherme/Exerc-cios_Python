nome = input('Que bom saber sobre seu aumento: ')
salário =float(input('{}, poderia me dizer quanto ganhava antes? '.format(nome)))
aumento =(salário+(salário*0.15))
print('Parabéns, {}, seu novo salário será creditado no valor de {:.4}'.format(nome, aumento))
