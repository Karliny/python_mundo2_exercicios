#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: - o primeiro valor é maior - o segundo valor é maior - não existe valor maior, os dois são iguais
primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))
if primeiro > segundo:
    print('O primeiro valor é maior que o segundo.')
elif primeiro == segundo:
    print('Não existe valor maior, os dois são iguais.')
else:
    print('O segundo valor é maior que o primeiro.')