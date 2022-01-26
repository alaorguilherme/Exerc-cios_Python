nome = str(input('Olá, poderia digitar seu nome: '))
n = int(input('Muito bem, {}, poderia me dizer um número inteiro para eu tentar descobrir se ele é ímpar ou par: '.format(nome)))
resultado = n%2
if resultado == 0:
    print('Seu número é PAR')
else:
    print('Seu número é ÍMPAR')