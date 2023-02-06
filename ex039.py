#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade: se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar, se já passou  do tempo do alistamento. Seu programa deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

sexo = (str(input('Você é homem ou mulher? \n M \n H \n Digite a opção:'))).upper()
if sexo == 'M':
    print('Você não tem obrigatoriedade de se alistar')
else:
    atual = date.today().year
    nasc = int(input('Ano de nascimento: '))
    idade = (atual - nasc)
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
    if idade == 18:
        print('Você deve se alistar IMEDIATAMENTE')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento.'.format(saldo))
        print('Seu alistamento será no ano de {}' .format(atual + saldo))
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos.'.format(saldo))
        print('Seu alistamento foi em {} ano'.format(atual - saldo))