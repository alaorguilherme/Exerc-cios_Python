nome = str(input('Olá, poderia digitar seu nome: ')).strip()
s = float(input('Muito bem, {}, poderia digitar seu salário atual: R$ '.format(nome)))
if s > 1250.00:
    print('Parabéns, {}, seu salário de {:.2f}, passará a ser: {:.2f}'.format(nome, s, s+(s*0.10)))
else:
    print('Parabéns, {}, seu salário de {:.2f}, passará a ser: {:.2f}'.format(nome, s, s+(s*0.15)))