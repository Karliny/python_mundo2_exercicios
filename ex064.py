#Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuario digitar o valor 999 que é a condição de parada. No final mostre quantos numeros foram digitados e qual foi a soma entre eles.
num = 0
soma = -999
contador = -1 
while num != 999:
    num = int(input('Digite valores para tratamento. Se quiser parar digite 999 \n'))
    soma = (num + soma) 
    contador += 1
print('Você digitou {} números e a soma entre eles foi de {}' .format(contador, soma))
print('FIM')

#forma passada pelo guanabara com correção:
'''num = soma = contador = 0
num = int(input('Digite valores para tratamento. Se quiser parar digite 999 \n'))
while num != 999:
        soma = (num + soma) 
    contador += 1
    num = int(input('Digite valores para tratamento. Se quiser parar digite 999 \n'))
print('Você digitou {} números e a soma entre eles foi de {}' .format(contador, soma))
print('FIM')''''''