# Ler distância de uma viagem em Km. Calcular o preço da passagem em R$0,50 apra viagens até 200Km e 0,45 para maiores.
import locale
locale.setlocale(locale.LC_ALL, '')
v1 = float(0.5)
v2 = float(0.45)
d = float(input('Distância da viagem em Km: '))
if d <= 200:
    pf = (d * v1)
    pf = locale.currency(pf)
    print('Sua viagem de {:g}Km custará {}'.format(d, pf))
else:
    pf = (d * v2)
    pf = locale.currency(pf)
    print('Sua viagem de {}Km custará {}'.format(d, pf))