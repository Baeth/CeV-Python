# ler NOME, IDADE e SEXO de 4 pessoas. Output:
# Média de idade do grupo;
# Nome do HOMEM mais velho;
# Quantas mulheres tem menos de 20 anos;

nome = []
idade = []
sexo = []

# Nesse exercício resolvi colocar algumas validações para os campos a serem preenchidos.
# Vou usar o método do "TRY", que aprendi estudando nuns exercícios anteriores.

for f in range(1, 5):
	print(f'-== {f}° Pessoa: ==-')
	nome.append(input(f'Nome: ').strip())
	while True:  # Loop em caso de erro.
		try:
			i = int(input(f'idade: ').strip())
			if i < 0:
				raise ValueError
			else:
				idade.append(i)
				break
		except ValueError:
			print("Parece que você não digitou uma idade corretamente.")
	while True:  # Loop em caso de erro.
		try:
			s = (input(f'sexo [m, f]: ').strip())
			print(s)
			if s != 'm' and s != 'f':
				raise ValueError
			else:
				sexo.append(s)
				break
		except ValueError:
			print("Parece que você não digitou o que pedi...")

# Calculeichons
m_index = [x for x in range(len(sexo)) if sexo[x] == 'm']  # Lista de MATCHOS
f_index = [x for x in range(len(sexo)) if sexo[x] == 'f']  # Lista de FEMME FATALE
	# Listas
m_idade = []
m_nome = []
f_nome = []
f_idade = []
f_idade20 = []

	# Filtrando homens e mulheres
for f in m_index:
	m_idade.append(idade[f])
	m_nome.append(nome[f])
for f in f_index:
	f_idade.append(idade[f])
	f_nome.append(nome[f])

	# Listando Novinhas
print(f_idade)
for f in range(len(f_idade)):
	if f_idade[f] < 20:
		f_idade20.append(f_idade[f])

# Respostas

print(f'A média de idade do grupo é {(sum(idade) / len(nome)):g}')
print(f'O nome do homem mais velho é {m_nome[m_idade.index(max(m_idade))]}')
print(f'Mulheres abaixo dos 20 anos: {len(f_idade20)}.')
