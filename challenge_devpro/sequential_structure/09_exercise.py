"""
Make a Program that asks for the temperature in degrees Fahrenheit, transform and display the temperature in degrees
Celsius. C = 5 * ((F-32) / 9).
########################################################################################################################
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""

fahrenheit = float(input('Enter the temperature in degrees Fahrenheit: '))
celsius = 5 * ((fahrenheit-32) / 9)

print(f'{fahrenheit} Fahrenheit is equal {round(celsius,2)} Celsius')
