# Ler velocidade de um carro. Se velocidade > 80km/h, informar multa no valor de R$ 7,00 por km acima do limite
import locale
locale.setlocale(locale.LC_ALL, '')
l = float(80)
m = float(7)
v = float(input('Velocidade: '))
if v > l:
    mf = ((v - l) * m)
    mf = locale.currency(mf)
    print('Sua velocidade está acima do limite permitido. Sua multa é de {}'.format(mf))
else:
    print('Parabéns! Você está dentro do limite de velocidade.')