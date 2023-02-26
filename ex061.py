#Refaça o desafio 51, lendo o primeiro termo de uma PA, mostrando os 10 primeiros termos da PA utilizando a estrutura while
print('='*30)
print('     10 TERMOS DE UMA PA    ')
print('='*30)
prim  = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
termo = prim
contador = 1
while contador <= 10:
  print('{} -> ' .format(termo), end=' ')
  termo = termo + razão
  contador = contador + 1
print('FIM!')