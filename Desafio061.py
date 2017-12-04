# Refazer desafio 51 usando WHILE
# 51: ler o Primeiro Termo e a Razão de uma PA. Mostrar os 10 primeiros termos dessa progressão.


pa = [int(input('Digite o primeiro termo de sua PA: '))]
r = int(input('E qual seria a razão?: '))

# Usando FOR
# for f in range(1, 10):
# 	pan = pa[0] + f * r
# 	pa.append(pan)
# print(f'Números da PA: {pa}')


# Usando WHILE
c = 1
pan = pa[0]
while c < 10:
	pan = pan + r
	pa.append(pan)
	c += 1
print(f'Números da PA: {pa}')
# Usar a mesta estrutura do FOR, adicionando a linha "c+= 1", também funciona.

# Também da pra imprimir cada linha da PA.
# c = 1
# print('a{} = {}'.format(1, pa[0]))
# while c < 10:
# 	print('a{} = {}'.format(c + 1, pa[0] + c * r))
# 	c += 1
