nome = str(input('Olá, poderia digitar seu nome: '))
A, B, C = input('Poderia digitar três números com espaço entre eles: ').split()
n, n1, n2 = [int(A), int(B), int(C)]
max = n
if n1 > max:
    max = n1
if n2 > max:
    max = n2
min = n
if n1 < min:
    min = n1
if n2 < min:
    min = n2
print('O maior número desses três é {}'.format(max))
print('O menor número desses três é {}'.format(min))

