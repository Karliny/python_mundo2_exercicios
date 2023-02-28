#programa q leia a idade e o sexo de varias pessoas a vada cadastro o programa deve perguntar se o usuario quer continuar
#ao final mostre: quantas pessoas tem mais de 18, quantos homens foram cadastrados, quantas mulheres tem menos de 20

escolha = ''
maiores = homens = qtdmulher = 0
while escolha != 'n':
  nome = str(input('Qual o nome: '))
  idade = int(input('Digite a sua idade: '))
  sexo = str(input('Digite o seu sexo: ')).strip().upper()[0]
  if idade > 18:
    maiores = maiores + 1
  if sexo == 'M':
    homens = homens + 1
  if sexo == 'F' and idade < 20:
    qtdmulher = qtdmulher + 1
  escolha = str(input('Você gostaria de continuar? s/n '))
  if escolha == 'n':
    break
    
print(f'Foram cadastradas {maiores} pessoas maiores de 18 anos. \nForam cadastrados {homens} homens. \nE foram cadastradas {qtdmulher} mulheres com idade inferior a 20 anos')

#PROGRAMA DO PROFESSOR:
'''tot18 = totH = totM20 = 0
while True:
    idade = int(input('Digite a idade: ')) 
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Qual o sexo? M/F ')).strip().upper()[0]
    if idade > 18:
        tot18 = tot18 + 1
    if sexo == 'M':
        totH = totH + 1
    if sexo == 'M' and idade < 20:
        totM20 = totM20 + 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você quer continuar? S/N '))
    if resp == 'N':
            break
    
    
print(f'Foram cadastradas {tot18} pessoas maiores de 18 anos. \nForam cadastrados {totH} homens. \nE foram cadastradas {totM20} mulheres com idade inferior a 20 anos')'''