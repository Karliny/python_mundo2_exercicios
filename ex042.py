#Criar programa que leia 3 segmentos e diga se pode ou não formar triângulo e qual tipo de triângulo
seg1 = float(input('Digite o primeiro segmento: '))
seg2 = float(input('Digite o segundo segmento: '))
seg3 = float(input('Digite o terceiro segmento: '))

if seg1 + seg2 < seg3 and seg2 + seg3 < seg1 and seg1 + seg3 < seg2:
  print('Os segmentos podem formar um triângulo!')
  if seg1 == seg2 and seg2 == seg3:
    print('O triângulo poderá ser Equilátero!')
  elif seg1 != seg2 and seg2 != seg3 and seg1 != seg3:
    print('O triângulo pode ser Escaleno!')
  else:
    print('O triângulo poderá ser Isósceles!')
else:
  print('Os segmentos não podem formar triângulo!')

#outra forma de escrever as condicionais:
# seg1 == seg2 == seg3
# seg1 != seg2 != seg3 != seg1