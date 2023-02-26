#Melhores o jogo do DESAFIO 028. Onde o computador vai pensar um numero, mostrando no final quantos palpites foram necessarios ate acertar
from random import randint
from time import sleep
computador = randint(0,10)
contador = 0
acertou = False
print('--.--' * 10)
print('Vou pensar em um número de 0 a 10, tente adivinhar: ')
print('--.--' * 10)

while not acertou:
  jogador = int(input('Qual é o seu palpite? '))
  contador += 1
  if jogador == computador:
    print('Parabéns, você acertou com {} tentativas'           .format(contador))
    acertou = True
  else:
    if jogador < computador:
      print('Mais...')
    elif jogador > computador:
      print('um pouco menos...')