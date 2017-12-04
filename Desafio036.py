# Programa que pergunte o valor de uma casa, o salário do cara e em quantos anos ele vai pagar.
# Calcular o valor da parcela, sendo que o empréstimo não é aprovado se exceder 30% do salário.
import locale
locale.setlocale(locale.LC_ALL, '')
v = input('Digite respectivamente o seu Salário, valor da casa, e em quantos anos quer pagar: ').split()
s, c, t = float(v[0]), float(v[1]), float(v[2])
tm = t * 12
p = c / tm
if p <= (s / 100) * 30:
	print('Parabéns! Seu crédito de {} foi \033[34m{}\033[m. Sua parcela é de {} ao mês, durante {:g} meses.'.format(locale.currency(c), 'APROVADO', locale.currency(p), tm))
else:
	print('Infelizmente seu crédito não pode ser aprovado com as informações fornecidas. ')