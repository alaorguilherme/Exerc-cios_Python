nome = str(input('Olá, poderia digitar seu nome: '))
km = float(input('Muito bem, {}, digite os kms da viagem: '.format(nome)))
if km <= 200:
    print('Sua viagem sairá no valor de: R${:.2f}'.format(0.50*km))
else:
    print('Sua viagem estará saindo pelo valor de: R${:.2f}.'.format(0.45*km))