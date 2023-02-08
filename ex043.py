#Crie um programa que calcule o IMC e mostre o resultado e classificação

peso = float(input('Qual é o seu peso em kg? '))
altura = float(input('Qual é a sua altura? '))
calculo = peso / altura ** 2
if calculo < 18.5:
  print('Seu IMC é {:.2f} e você está abaixo do peso.' .format(calculo))
elif calculo < 24.9:
  print('Seu IMC é {:.2f} e você está no peso normal.' .format(calculo))
elif calculo < 29.9:
  print('Seu IMC é {:.2f} e você está com sobrepeso.' .format(calculo))
elif calculo < 34.99:
  print('Seu IMC é {:.2f} e você está com obesidade grau I.' .format(calculo))
elif calculo < 39.99:
  print('Seu IMC é {:.2f} e você está com obesidade grau II (severa).' .format(calculo))
else:
  print('Seu IMC é {:.2f} e você está com obesidade grau III (mórbida).' .format(calculo))