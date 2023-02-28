#Crie um programa que simule um caixa eletronico. Pergunte ao usuario qual valor a ser sacadao (inteiro), o programa vai informar quantas cédulas de cada valor serao entregues, considerar que o caixa possui cedulas de 50, 20, 10 e 1 

#modo que eu criei:
num = 0
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

num = int(input('Digite o valor que deseja sacar: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
if u > 0:
    print(f'Serão {u} cédulas de 1 real')
if d > 0:
    print(f' e {d} cédulas de 10 Reais')
if c > 0:
    print(f' e {c*2} cédulas de 50 reais')

