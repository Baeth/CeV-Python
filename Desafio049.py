# Refazer o desafio 009 mostrando a tabuada de um número que o usr escolher, utilizando um laço FOR.
print('Tabuadinha do amor, de 1 a 10!')
t = int(input('Digite o número desejado: '))
for n in range(0, 10):
	print(f'{t} x {n + 1} = {t * (n + 1)}')
