#crie um programa que leia dois valores e mostre um menu na tela: 1 somar, 2 multiplicar, 3 maior, 4 novos números, 5 sair do programa
from time import sleep
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
escolha = 0
while escolha != 5:
  escolha = int(input('Digite a sua escolha: \n[1] - Somar \n[2] - Multiplicar \n[3] - Maior \n[4] - Novos Números \n[5] - Sair do programa \nSua opção: '))
  if escolha == 1:
    print('A soma entre {} e {} é de: {} '     
    .format(valor1,valor2, valor1 + valor2))
  elif escolha == 2:
    print('A multiplicação entre {} e {} é de: {} ' 
   .format(valor1,valor2, valor1 * valor2))
  elif escolha == 3:
    if valor1 > valor2:
      print('O maior valor é {}' .format(valor1))
    else:
      print('O maior valor é {}' .format(valor2))
  elif escolha == 4:
    valor1 = int(input('Digite novo primeiro valor: '))
    valor2 = int(input('Digite novo segundo valor: '))
  elif escolha == 5:
    print('Finalizando...')
  else:
    print('Opção inválida!')
sleep(1)
print('Fim do programa!')