# Faça um porgrama que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math
angle = float(input('Digite o ângulo a ser calculado: '))
cos = math.cos(angle)
sen = math.sin(angle)
tan = math.tan(angle)
print('Valores:')
print('Cosseno: {}'.format(cos))
print('Seno: {}'.format(sen))
print('Tangente: {}'.format(tan))
