# Programa que faz uma contagem regressiva para o estouro dos fogos de artifício de 10 até 0, com uma pausa de 1 segundo entre eles.
import time
import emoji
print('Contagem regressiva para os fogos de artifício!')
for t in range(10, 0, -1):
	print(f'{t}...')
	time.sleep(1)
print(emoji.emojize(':fireworks: :sparkler:', use_aliases=True))
