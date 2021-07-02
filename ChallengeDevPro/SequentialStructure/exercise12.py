"""
Using a person's height as input, build an algorithm that calculates their ideal weight using the following
formula: (72.7*height) - 58
########################################################################################################################
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte
fórmula: (72.7*altura) - 58
"""

height = float(input('Enter your height: '))
print("Your ideal weight is: ", round((72.7*height) - 58, 2))