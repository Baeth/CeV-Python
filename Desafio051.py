# ler o Primeiro Termo e a Razão de uma PA. Mostrar os 10 primeiros termos dessa progressão.
pa = [int(input('Digite o primeiro termo de sua PA: '))]
r = int(input('E qual seria a razão?: '))
for f in range(1, 10):
	pan = pa[0] + f * r
	pa.append(pan)
print(f'Números da PA: {pa}')
