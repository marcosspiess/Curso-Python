# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input('Informe um numero de 1 ate 9999: '))
print('Analisando o número {}'.format(num))
print('Unidade {}'.format(num // 1 % 10))
print('Dezena {}'.format(num // 10 % 10))
print('Centena {}'.format(num // 100 % 10))
print('Milhar {}'.format(num // 1000 % 10))
