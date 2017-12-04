# Ler o ano de nascimento do usuário:
# Se ele ainda vai se alistar;
# Seé a hora de se alistar;
# Se já passou do tempo de alistamento;
# O programa tamém tem que mostrar o tempo que falta para o alistamento, ou o quanto já passou.
import datetime
data = datetime.date.today()
# dia = int(data.day)
# mes = int(data.month)
ano = int(data.year)
nascano = int(input('Digite seu ano de nascimento: '))
dalistamento = ano - nascano

if dalistamento < 18:
	print(f'Você ainda não deve se alistar. Restam { 18 - dalistamento} ano(s).')
elif dalistamento == 18:
	print('Dezoitão, hein!? Vai comemorar numa junta militar mais próxima a você. Está na hora do alistamento!')
elif dalistamento > 18:
	print(f'Você DEVE se alistar! Você já está atrasado em {dalistamento - 18} ano(s).')