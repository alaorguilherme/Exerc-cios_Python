from datime import date as dt
nome = str(input('Olá, usuário, digite seu nome: ')).strip()
ano = int(input('{}, agora digite o ano que deseja verificar, caso queira verificar o ano atual digite 0: '.format(nome)))
if ano == 0:
    ano = dt.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Temos um ano bissexto!')
else:
    print('Não temos um ano bissexto!')