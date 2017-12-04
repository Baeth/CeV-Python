# Programa que leia seis números inteiros e mostre apenas os valores pares.
lista = input('Digite seis números(separados por espaço) que te direi quem és par: ').split()
par = []
print('Sua lista:', lista)
for a in lista:
	a = int(a)
	n = int(lista[a - 1])
	if n % 2 == 0:
		par.append(n)
print(f'Números pares: {par}')
