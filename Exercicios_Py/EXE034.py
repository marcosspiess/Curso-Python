# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
# o aumento é de 15%.

salário = float(input('Qual seu salário? R$'))
if salário > 1250:
    salário = (salário * 10 / 100)
else:
    salário = (salário * 15 / 100)
print('Você vai receber um aumento de R${:.2f}'.format(salário))