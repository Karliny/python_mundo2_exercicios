#Desenvolva um programa que leia nome, idade e sexo de 4 pessoas e mostre: a médica das idades, nome do homem mais velho, quantas mulheres tem menos de 20 anos.
somaidade = 0
maioridadehomem = 0
nomevelho = ''
qtdmulher = 0
for p in range (1,5):
    print('{} pessoa' .format(p))
    nome = str(input('Qual o nome: ')).strip()
    idade = int(input('Qual a idade: '))
    sexo = str(input('Qual o sexo: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
      maioridadehomem = idade
      nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
      maioridadehomem = idade
      nomevelho = nome
    if idade < 20 and sexo in 'Ff':
      qtdmulher = qtdmulher + 1
media = (somaidade/4)
print('A média de idade do grupo é de {} anos' .format(media))
print('O homem mais velho tem {} anos e se chama {}' .format(maioridadehomem, nomevelho))
print('A quantidade de mulheres com menos de 20 anos é de: {} ' .format(qtdmulher))