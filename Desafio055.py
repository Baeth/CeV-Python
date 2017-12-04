# ler o peso de 5 pessoas e dizer qual o maior, e o menor deles.
seq = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto']
peso = []
for f in range(0, 5):
	peso.append(input(f'Digite o {seq[f]} peso: '))
print(f'O peso máximo foi {max(peso)}Kg')
print(f'O peso mínimo foi {min(peso)}Kg')
