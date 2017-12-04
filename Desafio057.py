# ler SEXO de uma pessoa, aceitando somente "M" ou "F".
# Caso esteja errado, peça que digite novamente.

ok = 0
while ok == 0:
	sexo = input('Digite seu sexo ("M" ou "F"): ').upper()
	if sexo == 'M' or sexo == 'F':
		ok = 1
	else:
		print('Algo deu errado. Digite novamente, por favor.')