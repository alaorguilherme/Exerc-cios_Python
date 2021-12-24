nome =input('Boa tarde, poderia me dizer o seu nome? ')
largura =float(input('Muito bem, {}, quantos metros de largura tem a parede que você irá pintar? '.format(nome)))
altura =float(input('E qual seria a altura da parede? '))
área =(altura*largura)
tinta =int(área/2)
print('Como essa parede tem {}m² de área, precisaremos de {} litros de tinta para pintá-la'.format(área, tinta))

