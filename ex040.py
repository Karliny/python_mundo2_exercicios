#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: média abaixo de 5.0: reprovado, média entre 5.0 e 6.9: recuperação, media 7.0 superior: aprovado
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota1 + nota2) / 2
print('Sua média foi:{}' .format(média))
if média <= 5.0:
    print('Reprovado!')
elif média >= 7.0:
    print('Aprovado!')
else:
    print('Recuperação!')
