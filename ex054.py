#Crie um programa que leia o ano de nascimento das pessoas e determine se são maiores ou menores de idade
from datetime import date
atual = date.today().year
menor = 0
maior = 0
for c in range (0,7):
    nascimento = int(input('Qual o ano de nascimento? '))
    idade = (atual - nascimento)
    if idade <= 18:
        menor += 1
    elif idade > 18:
        maior += 1
print('{} pessoas são menores de idade e {} são maiores de idade' .format(menor, maior))
