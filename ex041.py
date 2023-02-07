from datetime import date

nasc = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year
idade = atual - nasc
print('O atleta tem {} anos.' .format(idade))

if idade <= 9:
    print('CLASSIFICAÇÃO: MIRIM')
elif idade > 9 and idade < 14:
    print('CLASSIFICAÇÃO: INFANTIL')
elif idade > 14 and idade < 19:
    print('CLASSIFICAÇÃO: JUNIOR')
elif idade > 19 and idade < 25:
    print('CLASSIFICAÇÃO: SÊNIOR')
else:
    print('CLASSIFICAÇÃO: MASTER')

#outra forma simplificada:
from datetime import date

nasc = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year
idade = atual - nasc
print('O atleta tem {} anos.' .format(idade))

if idade <= 9:
    print('CLASSIFICAÇÃO: MIRIM')
elif idade <= 14:
    print('CLASSIFICAÇÃO: INFANTIL')
elif idade <= 19:
    print('CLASSIFICAÇÃO: JUNIOR')
elif idade <= 25:
    print('CLASSIFICAÇÃO: SÊNIOR')
else:
    print('CLASSIFICAÇÃO: MASTER')