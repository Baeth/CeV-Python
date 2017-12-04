# Ler um número e mostrar seu fatorial
# Solução usando WHILE e FOR

n = int(input('Digite um número, que vou mostrar seu fatorial: '))
r = n - 1  # contador
nf = n

# calcular

while r >= 1:
    nf = nf * r
    r = r - 1

# for f in range(r, 1, -1):
#     nf = nf * f

print('{}! = {}'.format(n, nf))