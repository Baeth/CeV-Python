#ler qualquer coisa e mostrar todas as informações sobre o que foi digitado
Qisso = input('Digite qualquer coisa: ')
print('Tipo primitivo: {}'.format(type(Qisso)))
print('Tem espeços?: {}'.format(Qisso.isspace()))
print('É um número: {}'.format(Qisso.isnumeric()))
print('É alfabético?: {}'.format(Qisso.isalpha()))
print('É alfanumérico?: {}'.format(Qisso.isalnum()))
print('Está em maiúsculas: {}'.format(Qisso.isupper()))
print('Está em minúsculas?: {}'.format(Qisso.islower()))
print('Está capitalizada?: {}'.format(Qisso.istitle()))
