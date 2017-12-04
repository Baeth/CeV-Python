# Ler o ano de nascimento do atleta e mostrar sua categoria:
# Até 9 anos: MIRIM;
# Até 14 anos: INFANTIL;
# Até 19 anos: JUNIOR;
# Até 20 anos: SÊNIOR;
# Acima de 20: MASTER
import datetime
data = datetime.date.today()
dia = int(data.day)
mes = int(data.month)
ano = int(data.year)
nasc = int(input('Digite seu ano de nascimento: '))
idade = ano - nasc
print('Você tem {} anos.'.format(idade))
if idade <= 9:
	print('Sua categoria é: MIRIM')
elif 14 >= idade > 9:
	print('Sua categoria é: INFANTIL')
elif 19 >= idade > 14:
	print('Sua categoria é: JUNIOR')
elif idade == 20:
	print('Sua categoria é: SÊNIOR')
elif idade > 20:
	print('Sua categoria é: MASTER')
