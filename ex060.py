#Faça um programa que leia um número qualquer e mostre o seu fatorial
num = int(input('Digite um número para que ele seja fatorado: '))
contador = num
f = 1
while contador > 0:
  print('{}' .format(contador), end=' ')
  print(' x ' if contador > 1 else ' = ', end=' ')
  f *= contador
  contador = contador - 1  
print('{}' .format(f))