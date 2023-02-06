#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 - binario, 2- octal e 3- hexadecimal
num = int(input('Digite um número inteiro qualquer: '))
escolha = int(input('Escolha a conversão: \n 1 - para Binário \n 2 - para Octal \n 3 - para Hexadecimal \n Sua opção: '))
if escolha == 1:
    print('{} convertido para binario é igual a {}' .format(num, bin(num)[2:]))
elif escolha == 2:
      print('{} convertido para octal é igual a {}' .format(num, oct(num)[2:]))
elif escolha == 3:
      print('{} convertido para hexadecimal é igual a {:}' .format(num, hex(num)[2:]))
else:
    print('Digite um número válido de escolha de conversão')
