# Sortear 1 aluno entre quatro. O resultado deverá ser o nome do aluno.
import random
a = input('Digite o nome dos alunos separados por vírgula: ').split(", ")
print('O nome do sortudo(a) é {}!'.format(random.choice(a)))
