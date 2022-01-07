# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# considere US$1,00 = R$5,58

real = float(input('Quando dinheiro você tem na carteira? '))
dolar = real / 5.58
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
