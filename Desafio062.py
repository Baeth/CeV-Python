# Melhorar o desafio 61, que veio do 51. Perguntar ao usr se ele quer adicionar mais alguns termos.
# O programa encerra quando ele deseja adicionar mais "0" termos.


# Só foi atualizado o primeiro código WHILE. Preguiça =P

pa = [int(input('Digite o primeiro termo de sua PA: ').strip())]
r = int(input('E qual seria a razão?: '))
# Usando FOR
# for f in range(1, 10):
# 	pan = pa[0] + f * r
# 	pa.append(pan)
# print(f'Números da PA: {pa}')


# Usando WHILE
c = 1  # contagem. Começando em 1 Pq já temos o primeiro termo.
pan = pa[0]
limite = 10  # Limite de repetições
while c < limite:
	pan = pan + r
	pa.append(pan)
	c += 1
	if c == limite:
		print(f'Números da PA: {pa}')
		limite = int(input('Gostaria de ver mais termos da PA? Quantos?: ').strip())
		c = 0
	if limite == 1:
		exit()

# Usar a mesta estrutura do FOR, adicionando a linha "c+= 1", também funciona.

# Também da pra imprimir cada linha da PA.
# c = 1
# print('a{} = {}'.format(1, pa[0]))
# while c < 10:
# 	print('a{} = {}'.format(c + 1, pa[0] + c * r))
# 	c += 1
