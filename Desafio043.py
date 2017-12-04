# Ler o Peso e a Altura; Calcular IMC e mostrar o status conforme lista:
# Abaixo de 18.5: Abaixo do Peso;
# Entre 18.5 e 25: Peso ideal;
# Entre 25 e 30: Sobrepeso;
# Entre 30 e 40: Obesidade;
# 40+: Obesidade mórbida;
peso = int(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = float(peso / altura ** 2)
if imc < 18.5:
	print(f'Seu IMC é {imc:.2f}: Abaixo do peso')
elif 25 > imc >= 18.5:
	print(f'Seu IMC é {imc:.2f}: Peso ideal')
elif 30 > imc >= 25:
	print(f'Seu IMC é {imc:.2f}: Sobrepeso')
elif 40 > imc >= 30:
	print(f'Seu IMC é {imc:.2f}: Obesidade')
elif imc >= 40:
	print(f'Seu IMC é {imc:.2f}: Obesidade Mórbida')
