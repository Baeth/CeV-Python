# Calcular a SOMA de todos os números ÍMPARES entre 1 e 500
lista = []
print('Mostrando a SOMA de todos os números ÍMPARES entre 1 e 500:')
for n in range(1, 501, 2):
	if n % 3 == 0:
		lista.append(n)
print(sum(lista))
