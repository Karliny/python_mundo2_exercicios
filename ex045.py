from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('''Escolha um ítem:
[0] Pedra
[1] Papel
[2] Tesoura
Digite sua escolha: '''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print('-=' * 10)
print('Computador escolheu {}' .format(itens[computador]))
print('Jogador escolheu {}' .format(itens[jogador]))
print('-=' * 10)
if computador == 0: #Pedra
  if jogador == 0:
    print('Empate!')
  elif jogador == 1:
    print('Jogador VENCE!')
  elif jogador == 2:
    print('Computador VENCE!')
  else:
    print('Jogada inválida!')
elif computador == 1: #Papel
  if jogador == 0:
    print('Computador VENCE!')
  elif jogador == 1:
    print('Empate!')
  elif jogador == 2:
    print('Jogador VENCE!')
  else:  
    print('Jogada inválida!')
elif computador == 2: #Tesoura
  if jogador == 0:
    print('Jogador VENCE!')
  elif jogador == 1:
    print('Computador VENCE!')
  elif jogador == 2:
    print('Empate!')
  else:
    print('Jogada inválida!')