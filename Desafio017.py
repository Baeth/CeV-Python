# Faça um porgrama que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo. Calcule e mostre o comprimento da hipotenusa
import math
catOposto = float(input('Digite o comprimento do cateto oposto: '))
catAdjacente = float(input('Digite o comprimento do cateto adjacente: '))
resultado = math.hypot(catAdjacente, catOposto)
print('O valor da hipotenusa é {}. =)'.format(resultado))
