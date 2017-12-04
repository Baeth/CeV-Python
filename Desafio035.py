# Ler 3 comprimentos de reta e dizer se eles podem formar um triângulo
print('Digite três comprimentos de reta separados por espaço, e eu te direi se pode fazer um triângulo.')
n = (input().split())
# n = [float(lf) for lf in n]
a = float(n[0])
b = float(n[1])
c = float(n[2])
# -- Condição de existência
if (a - b) < c < a + b:
	tri = True
else:
	tri = False
# --
if tri == True and(a == b == c):
	print('Isso ai pode dar num triângulo equilátero!')
elif tri == True and(a == b or a == c or b == c):
	print('Isso ai pode dar num triângulo isósceles!')
elif tri == True and(a != b != c):
	print('Isso ai pode dar num triângulo escaleno!')
else:
	print('Com essas medidas aí, nem rolou!')
