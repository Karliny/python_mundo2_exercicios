#Melhore o desafio 061 perguntando se o usuário quer mostrar mais alguns termos. O programa deve encerrar quando o usuario quiser msotrar 0 termos
print('='*30)
print('     10 TERMOS DE UMA PA    ')
print('='*30)
prim  = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
termo = prim
contador = 1
total = 0
mais = 10
while mais != 0:
  total = total + mais
  while contador <= total:
    print('{} -> ' .format(termo), end=' ')
    termo = termo + razão
    contador = contador + 1
  mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão encerrada com  {} termos mostrados' .format(total))
