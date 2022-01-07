# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de
# 2 metros quadrados.

larg = float(input('Largura da sua parede: '))
alt = float(input('Altura da sua parede: '))
area = larg * alt
print('Sua parete tem a dimensão de {}x{} e sua área é de {}m²'.format(alt, larg, area))
tinta = area/2
print('Para pintar essa parede, você precisará de {}L de tinta. '.format(tinta))