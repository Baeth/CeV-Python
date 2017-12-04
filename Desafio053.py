# ler uma Frase e dizer se ela é Palíndroma*, REMOVENDO os espaços.
# *A frase/palavra pode ser dita ao contrário que acaba no mesmo.

frase = input('Digite uma frase aí. Vou escanear ela com meu palindrômetro: ')

# Temos que igualar todas as letras pra não dar erro na ora da comparação. EX: Asa != asA
# Para uma solução mais completa e abrangente, o certo seria remover também os caracteres especiais e pontuações.
frase_final = frase.replace(' ', '').lower()
# print(frase_final)  # Teste de varíavel

if frase_final[::-1] == frase_final:  # Determina um corte extendido: [Início:Fim:Saltos] -1 Saltos faz a order ser invertida.
	print('Temos aí um palindrômo. Nice!')
else:
	print("""Parece que não foi dessa vez.
	Frase:   {}
	Inverso: {}""".format(frase, frase[::-1]))

