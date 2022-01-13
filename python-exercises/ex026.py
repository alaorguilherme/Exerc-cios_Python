nome = str(input('Olá, poderia digitar seu nome: ')).strip()
frase = str(input('Muito bem, {}, poderia digitar uma frase qualquer: '.format(nome))).upper().strip()
print("""Pela minha análise sua frase há {} letras A
      ela aparece pela primeira vez na posição {}
      e pela última vez na posição {}.""".format(frase.count('A'), frase.find('A')+1, frase.rfind('A')+1))