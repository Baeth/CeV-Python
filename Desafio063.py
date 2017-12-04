# Pedir um número N e criar uma sequência de fibonacci com N elementos.

c = 0  # Contador
n = int(input('Digite um número limite para a sequência: ').strip())  # "n" servirá como limite do contador.
f1 = f2 = 1  # "f1" e "f2" serão os dois últimos termos na sequência
fibo = []  # Criar lista que será usada como resposta.

while c < n:
	f1, f2 = f2, f1 + f2
	fibo.append(f1)
	c += 1
print(*fibo, sep=' ➡ ')
