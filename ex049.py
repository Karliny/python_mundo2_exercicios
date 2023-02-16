#Recrie o programa do exercício 009, usando o laço for
num = int(input('Digite um número para saber sua tabuada: '))
print('-' * 15)
for c in range (0,11, +1):
    print('{} x {} = {} '.format(num, c, num*c))
print('-' * 15)