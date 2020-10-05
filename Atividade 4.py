"""Faça um programa que leia dois números e mostre qual o maior dos dois.
O programa deve informar caso sejam iguais."""

num01 = int(input('Digite um valor:'))
num02 = int(input('Digite um valor:'))

if num01 == num02:
    print('Os valores digitados são iguais')
elif num01 > num02:
    print('Maior número: {}'.format(num01))
elif num02 > num01:
    print('Maior número: {}'.format(num02))
