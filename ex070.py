#programa que leia preço de varios produtos. O programa deve perguntar se o usuario quer continuar. No final mostre: qual total gasto na compra, quantos produtos custam mais de 100 reais e qual é o nome do produto mais barato
produto = ''
preço = 0
resposta = 'S'
soma = 0
somamil = 0
menor = 0
nomeproduto = ''
contador = 0
while resposta == 'S':
    contador = contador + 1
    produto = str(input('Nome do produto: ')).capitalize()
    preço = float(input('Digite o valor do produto: '))
    if contador == 1:
        menor = preço
        nomeproduto = produto
    else: 
        if preço < menor:
            menor = preço
            nomeproduto = produto
    if preço >= 1000:
        somamil = somamil + 1
    if preço > 0:
        soma = soma + preço 
    resposta = str(input('Quer continuar? S/N ')).strip().upper()
print(f'O total gasto foi de {soma}')
print(f'Houveram {somamil} produtos que custam mais de 1000 Reais.')
print(f'{nomeproduto} foi o menor produto e custou {menor}.')
