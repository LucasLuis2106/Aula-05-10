"""Faça um programa para solicitar o nome e as duas notas e um aluno.
Calcular sua média e informá-la. Se ela for inferior a 7, escrever
"Reprovado”; caso contrário escrever "Aprovado"."""
Nome = input("Digite seu nome:")
nota1 = float(input('digite sua primeira nota:'))
nota2 = float(input('digite sua segunda nota:'))
media = (nota1 + nota2) / 2

print('Nome do aluno:', Nome)
print('-+-' * 30)
print('Média do aluno: ', media)
print('-+-' * 30)

if media >= 7:
    print('Aprovado')

else:

    if media >= 7:
        print('Aprovado')
    else:
        print('Reprovado')
print('-+-' * 30)
