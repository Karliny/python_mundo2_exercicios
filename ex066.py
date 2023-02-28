#Crie um programa que leia varios numeros inteiros e pare quando digitar 999. Fazendo a contagem e a soma dos numeros digitados

n = s = cont = 0
while True:
  n = int(input('Digite um valor: '))
  if n == 999:
      break
  s += n
  cont = cont + 1
    
print(f'Você digitou {cont} números e a soma entre eles é de {s}')