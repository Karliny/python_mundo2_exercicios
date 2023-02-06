#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal. Sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Valor da casa: '))
salário = float(input('Salário do comprador: '))
anos = int(input('Em quantos anos pretende pagar: '))
prestação = casa / (anos * 12)
if prestação > (salário * 30 / 100):
    print('Sua solicitação foi negada, o valor da prestação ultrapassa 30 por cento do salário.')
else:
    print('A prestação mensal será de R${:.2f}' .format(prestação))

