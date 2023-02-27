#Crie um programa que leia varios numeros inteiros e no final mostre a media entre todos, qual maior e qual menor. O programa deve perguntar se o usuario quer continuar a digitar numeros
escolha = 'S'
num = 0
contador = 0
maior = 0
menor = 0
soma = 0
while escolha == 'S':
  num = int(input('Digite um número: '))
  escolha = str(input('Quer continuar? s/n: ')).upper()
  contador += 1
  soma = soma + num
  if contador == 1:
    maior = num
    menor = num
  else:
    if num > maior:
      maior = num
    elif num < menor:
      menor = num
    
print('Você digitou {} numeros e a média entre eles é de {}'.format(contador, soma/contador))
print('O maior número digitado foi {} e o menor número digitado foi {}' .format(maior,menor))