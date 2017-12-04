# Upgrade do desafio 28.
# PS: Acabou que eu já tinha feito do jeito que ele está pedindo agora, então só copiei.
# Programa escolhe um número entre 0 e 5 e pergunta qual ele escolheu. Lembrar de mostrar se você venceu ou perdeu
from random import randint
import time
print('Estou escolhendo um número. Aposto que você não vai conseguir adivinhar...')
m = randint(0, 5)
time.sleep(5)
tentativa = 1
while tentativa == 1:
    t = int(input('Tenta aí! Um número entre 0 e 5: '))
    if m == t:
        print('Acertô, miseravi!')
        tentativa = 0
    else:
        print('Hoje não! Tenta de novo...')
