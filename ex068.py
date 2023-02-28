#programa em que o jogador e o computador jogam par ou impar, o programa para qnd jogador perde.
from random import randint
computador = randint(0,10)
contador = 0
while True:
  jogador = int(input('Digite um número: '))
  escolha = str(input('Você quer par ou ímpar? P/I  '))
  resultado = (jogador + computador) % 2
  if resultado ==0:
    final = 'par'
  else:
    final = 'ímpar'
  print (f'Você escolheu {jogador} e o computador escolheu {computador} que somando dá {computador+jogador}. Que é {final}')
  contador = contador + 1
  if escolha == final:
    print('Parabéns você acertou!')
    break
  else: 
    print(f'Você errou! Essa é a sua {contador} tentativa')

  #SOLUÇÃO MAIS CLEAN E ACERTADA:
  '''from random import randint
v = 0
while True:
  computador = randint(0,10)
  jogador = int(input('Digite um número: '))
  total = jogador + computador
  tipo = ' '
  while tipo not in 'IP':
    tipo = str(input('Você quer par ou ímpar? ')).strip().upper()[0]
  print(f'Você jogou {jogador} e o computador jogou {computador}. Que deu {total}.')
  if tipo == 'P':
    if total % 2 == 0:
        print('Você venceu!')
        v = v + 1
    else:
        print('Você perdeu!')
        break
  elif tipo == 'I':
    if total % 2 == 1:
        print('Você venceu!')
        v = v + 1
    else:
        print('Você perdeu!')
        break
    print('Vamos jogar novamente...')
print(f'Game over! Você venceu {v} vezes!')
 '''