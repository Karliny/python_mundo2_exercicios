#Faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario. O programa será interrompido quando o número solicitado for negativo
num = 0
c = 0
mais = 0
while True:
  num = int(input('Digite um número para ver sua tabuada: '))
  c = 0
  if num >=0:
    while c < 10:
      c = c + 1
      resul = (num*c)
      print(f'{num} x {c} = {resul}')
  elif num < 0:
    break
print('Seu programa chegou ao fim!')