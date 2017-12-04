# Programa que lê constantemente números digitados. O programa só para quando for digitado 999.
# No final, mostrar quantos números foram digitados e a soma deles., desconsiderando o "999".

soma = 0
n = 0

while True:
	v = int(input('Digite um número qualquer. Ou pressione 999 para parar: '))
	if v == 999:
		print('Você digitou {} número(s)'.format(n))
		print('A soma de todos eles é: {}'.format(soma))
		exit()
	else:
		n += 1
		soma = soma + v
