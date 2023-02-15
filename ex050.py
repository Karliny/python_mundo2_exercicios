#Crie um programa que leia quatro números e faça a somatória dos que forem par
soma = 0
for c in range (0,4):
    num = int(input('Digite um número: '))
    if num %2==0:
        soma = soma + num
print('a somatória dos números pares digitados é {}' .format(soma))