#Crie um programa que leia uma palavra e determine se ela é Palíndromo
frase = str(input('Digite uma palavra: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) - 1, - 1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('É um palíndromo!')
else:
    print('Não é palíndromo')

#outra forma de fazer:
# inverso = junto[::-1]