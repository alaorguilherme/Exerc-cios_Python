km = int(input('Olá, operador(a), quantos kms foram marcados na sua máquina: '))
if km <=80:
    print('Muito bem, ele está dentro da velocidade permitida!')
else:
    print('Infelizmente esse carro será mutado na quantia de R${}.'.format((km-80)*7))