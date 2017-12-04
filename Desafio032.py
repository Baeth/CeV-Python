# Fazer um programa que diz se um ano é bissexto.
# -- Ler o Ano e verificar input
while True:
    while True:
        try:
            a = int(input('Digite um ano: '))
            if a == 0: raise Exception
            break
        except ValueError:
            print("Parece que você não digitou um ano corretamente.")
        except Exception:
            print('"0" Não pode ser um ano. duhh...')
    # ---
    if a >= 400 and a % 4 == 0:
        if a % 100 == 0 and a % 400 == 0:
            b = 1
    if a < 400 and a % 4 == 0 and a != 0:
        if a % 100 == 0:
            b = 0
        if a < 100:
            b = 1
    else: b = 0
    print('Este é um ano bissexto.') if b == 1 else print('Este não é um ano bissexto')
