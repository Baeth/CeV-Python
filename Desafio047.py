# Mostrar todos os números pares entre 1 e 50
s = []
print('Mostrando números pares entre 1 e 50:')
for n in range(1, 51):
	if n % 2 == 0: s.append(n)
print(s)