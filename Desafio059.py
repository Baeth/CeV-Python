# Programa que lê dois valores e mostre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior Valor
# [4] Novos Números
# [5] Sair do Programa
# Todos os itens do menu devem ser funcionais.

# Armazenar valores
v = []
while len(v) != 2:
	v = (input('Digite dois valores, separados por um espaço: ').strip().split())
v = [int(v[0]), int(v[1])]

# Loop do Menu
escolha = 0
while escolha == 0:
	print("""Menu:
	[1] Somar
	[2] Multiplicar
	[3] Maior Valor
	[4] Novos Números
	[5] Sair do Programa
	""")
	estemp = int(input('Escolha uma opção: '))
	if estemp in range(1, 5):
		escolha = estemp
		if escolha == 4: # Novos números
			v = []
			while len(v) != 2:
				v = input('Digite dois valores, separados por um espaço: ').strip().split()
			v = [int(v[0]), int(v[1])]
			escolha = 0
	else:
		print('Escolha Inválida.')

# Início das funções

	# Soma
if escolha == 1:
	print('{} + {}: {}'.format(v[0], v[1], sum(v)))

	# Multiplicação
if escolha == 2:
	print('{} x {}: {}'.format(v[0], v[1], v[0] * v[1]))

	# Maior Valor
if escolha == 3:
	print(f'O Maior valor é {max(v)}')

	# Sair
if escolha == 5:
	print('Bai!')
	exit()