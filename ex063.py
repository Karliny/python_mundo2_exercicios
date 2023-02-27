#Escreva um programa que leia um numero e apresente os n primeiros elementos de uma sequencia Fibonacci
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} - {}' .format(t1,t2), end='')
contador = 3
while contador <= n:
  t3 = t1 + t2
  print(' - {} ' .format(t3), end='')
  contador += 1
  t1 = t2
  t2 = t3
print('\n FIM')