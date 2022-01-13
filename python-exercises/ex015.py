nome = input('Olá, bem vinda ao Aluguel de Carros Ajato, poderia me dizer seu nome: ')
km = float(input('Muito bem, {}, quantos Km pretendemos correr nesse belo dia: '.format(nome)))
d = int(input('E você pretende alugar um de nossos carros por quantos dias? '))
p = d * 60 + km * 0.15
print('Perfeito, {}. Essa empreitada estará saindo no valor de R${:.2f}'.format(nome, p))
