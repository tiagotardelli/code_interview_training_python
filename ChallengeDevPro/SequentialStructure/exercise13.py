"""
Taking as input the height (h) of a person, build an algorithm that calculates their ideal weight, using the
following formulas:
    a) For men: (72.7*h) - 58
    b) For women: (62.1*h) - 44.7
########################################################################################################################
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as
seguintes fórmulas:
    a) Para homens: (72.7*h) - 58
    b) Para mulheres: (62.1*h) - 44.7
"""

h = float(input('Enter your height'))
print('Ideal weight for men: ', round((72.7*h) - 58, 2))
print('Ideal weight for women: ', round((62.1*h) - 44.7, 2))
