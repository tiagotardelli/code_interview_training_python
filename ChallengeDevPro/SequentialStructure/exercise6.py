from math import pi

"""
Make a program that asks for the radius of a circle, calculate and show its area.
Pt-br > Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""

radius = float(input('Enter the radius of a circle: '))
area = pi*(radius**2)
print(f'The circle area is {round(area, 2)}')
