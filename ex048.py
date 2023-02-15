#Crie um programa que calcule a soma entre todos os números ímpares que são multiplos de 3 e que se encontram no intervalo de 1 a 500
soma = 0
for c in range (1,500,2):
    n = c
    if n %3==0:
        soma = soma + n
print(soma)