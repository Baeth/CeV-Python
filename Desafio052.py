# ler um Número e dizer se ele é Primo.
n = int(input('Digite um número que te digo se ele é primo: '))
dv = []
if n > 1:
	primo = 1
	for f in range(n - 1, 1, -1):
		if (n % f) == 0:
			# Essas linhas foram minha primeira tentativa. O bloco IF para quando encontra qualquer divisor no range.
			# Mas aí eu resolvi adicionar a funcionalidade os divisores do número.
			# print(f'{n} não é um número primo.')
			# print(f'{f} x {int(n / f)} = {n}')
			# break
			primo = 0
			dv.append(int(n / f))
	if primo == 1:
		print(f'{n} é um número primo')
	elif primo == 0:
		print(f'{n} Não é primo. Seus divisores são: {dv}')
else:  # Se o número >=1, ele não é primo.
	print(f'{n} não é um número primo.')
