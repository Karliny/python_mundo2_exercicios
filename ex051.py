#Crie um programa que leia o primeiro termo e a razão de uma PA e mostre os 10 primeiros termos
print('='*30)
print('     10 TERMOS DE UMA PA    ')
print('='*30)
prim  = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
for c in range (prim, prim + razão * 10, +razão):
    print('{}' .format(c))