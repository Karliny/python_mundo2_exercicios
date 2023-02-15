#Crie um programa que leia o primeiro termo e a razão de uma PA e mostre os 10 primeiros termos
prim  = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
for c in range (prim, prim + razão * 10, +razão):
    print(c)