# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
# formar um triângulo.

a = float(input('primeira reta'))
b = float(input('segunda reta'))
c = float(input('terceira reta'))

if c < a + b and a < b + c and b < a + c:
    print('pode formar um triangulo')
else:
    print('Não pode formar um triangulo')
    