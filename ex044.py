#Crie um programa que calcule o valor a ser pago por um produto considerando preço normal e condições de pagamento
print('{:=^40}' .format(' Lojas da Kah '))
valor = float(input('Insira o valor das compras: '))
pagamento = int(input('Digite a forma de pagamento: \n[1] à vista (dinheiro ou cheque) \n[2] à vista no cartão \n[3] 2x no cartão \n[4] 3x no cartão \nQual é a opção? '))
if pagamento == 1:
    print('Sua compra de R${} vai custar R${} no final' .format(valor, valor - ( valor * 10/100)))
elif pagamento == 2:
    print('Sua compra de R${} vai custar R${} no final' .format(valor, valor - ( valor * 5/100)))
elif pagamento == 3:
    print('Sua compra continua com o valor de R${}' .format(valor))
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {:.2f}x de {:.2f} reais e vai custar ao total R${}' .format(parcelas, (valor + ( valor * 20/100))/parcelas, valor + (valor * 20/100)))
else:
    print('Digite uma opção válida!')