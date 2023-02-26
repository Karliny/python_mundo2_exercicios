#Crie um programa que leia o sexo de uma pessoa, mas só aceite os valores m ou f. Caso esteja errado peça a digitação até ter um valor correto
sexo = str(input('Informe o seu sexo [M/F] ')).strip().upper()[0]
while sexo not in 'FM':
  print('Por favor, digite uma entrada válida [F] ou [M]')
  sexo = str(input('Dado inválido. Por favor digite M ou F: ')).strip().upper()[0]
if sexo == 'M':
  print('Sexo masculino registrado com sucesso!')
else:
  print('Sexo feminino registrado com sucesso!')