# Ler 3 números e mostrar qual deles é o maior e o menor
print('Digite três números separados por espaço, e eu te direi qual é o maior deles.')
n = (input().split())
n = [float(lf) for lf in n]
print('O maior número é {}. Já o menor, {}'.format(max(n), min(n)))
