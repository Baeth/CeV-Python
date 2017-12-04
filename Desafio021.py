# Ler o nome completo; Mostrar nome completo em maiúsculas e minúsculas; Quantas letras ao todo, sem contar espeços; Quantas letras tem o primeiro nome;
n = input('Digite seu nome completo: ')
nsplit = n.split()
t = len(n) - n.count(' ')
print('Nome minúsculo: {}'.format(n.lower()))
print('Nome minúsculo: {}'.format(n.upper()))
print('Seu nome completo contém {} letras.'.format(t))
print('Seu primeiro nome contém {} letras.'.format(len(nsplit[0])))
