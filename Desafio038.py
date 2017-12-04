# Programa que peça dois números inteiros, compare-os e mostre a seguinte mensagem:
# - O primeiro valor é maior.
# - O Segundo valor é maior
# - Não existe valor maior. Os dois são iguais.
fimc = '\033[m'
azul = '\033[34m'
roza = '\033[35m'
amarelo = '\033[33m'
vermelho = '\033[31m'
v1 = int(input('Digite o {}{}{} valor: '.format(azul, 'primeiro', fimc)))
v2 = int(input('Digite o {}{}{} valor: '.format(amarelo, 'segundo', fimc)))
if v1 > v2:
	print('O {}{}{} valor é o maior'.format(azul, 'primeiro', fimc))
elif v1 < v2:
	print('O {}{}{} valor é o maior'.format(amarelo, 'segundo', fimc))
elif v1 == v2:
	print('Não existe valor maior. Os dois são {}{}{}'.format(vermelho, 'iguais', fimc))
