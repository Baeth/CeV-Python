# Programa que lê constantemente números (int) digitados. O programa deve perguntar se deve parar de armazenar.
# No final, mostrar a média entre os números digitados e qual foi o maior / menor.

soma = 0
# Maior e menor estão como nulo.
# Caso fosse 0, e nunca houvessem digitado esse número, o menor seria 0 ao invéz do real menor número.
maior = None
menor = None
n = 0

while True:
	v = int(input('Digite um número qualquer: '))
	q = input('Gostaria de continuar adicionando números? (S/N): ').upper().strip()
	if q == 'S':
		soma = soma + v
		n += 1
		# Condicionais para tirar o valor nulo e não dar erro ao comparar com V.
		if maior == None: maior = v
		if menor == None: menor = v
		# Maior / Menor
		if v > maior:
			maior = v
		if v < menor:
			menor = v
	elif q == 'N':
		print('Maior número: {}'.format(maior))
		print('Menor número: {}'.format(menor))
		print('Média: {:g}'.format(soma / n))
		exit()
	else:
		print('Opção inválida. Herp Derp')
		q = input('Gostaria de continuar adicionando números? (S/N): ').upper().strip()
		# print('Continuando pra deixar de ser bobo...')
