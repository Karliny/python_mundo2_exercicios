#Crie programa que leia número inteiro e determine se ele é ou não PRIMO
print('='*30)
print('    SABER SE NÚMERO É PRIMO    ')
print('='*30)
tot = 0
num  = int(input('Digite um número: '))
for c in range (1, num + 1):
    if num % c == 0:
        tot += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
       
    print('{} ' .format(c), end='')
    
print(' \n\033[mO número {} foi divisível {} vezes' .format(num, tot))
if tot == 2:
    print('Esse número é primo')
else:
    print('Esse número não é primo')