#ler número e mostrar seu sucessor e o antecessor
n = int(input('Digite um número: '))
a = n-1
s = n+1
# print('O antecessor e o sucessor do número {} são, respectivamente, {} e {}'.format(n, a, s))
print('O antecessor e o sucessor do número {} são, respectivamente, {} e {}'.format(n, (n-1), (n+1)))