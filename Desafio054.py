# ler o Nascimento de 5 pessoas e dizer quantas pessoas são maiores e menores de idade.
maior = []
menor = []
for f in range(1, 8):
	i = int(input(f'Digite a idade da pessoa n°{f}: '))
	if i >= 18:
		maior.append(i)
	elif 18 > i >= 0:  # Comparação para não registrar idades negativas.
		menor.append(i)
	else:
		print('Com essa idade aí, ou a pessoa nunca existiu, ou já virou presunto! Não vou contar essa.')

# Testes das listas finais.
# print('Maior', maior)
# print('Menor', menor)

print(f'Temos {len(menor)} pessoas menores de idade e {len(maior)} na maioridade.')
