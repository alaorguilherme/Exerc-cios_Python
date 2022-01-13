n = int(input('Olá, poderia digitar um número de 0 a 9999: '))
m = n // 1000 % 10
c = n // 100 % 10
d = n // 10 % 10
u = n // 1 % 10
print('Analisando o número {}...'.format(n))
print(""""Unidade: {}
 Dezena: {}
 Centena: {}
 Milhar: {}""".format(u, d, c, m))
