"""
Make a Program that asks for the temperature in degrees Celsius, transform and display it in degrees Fahrenheit.
########################################################################################################################
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""

celsius = float(input('Enter the temperature in degrees Celsius: '))
fahrenheit = ((celsius-32) * 5) / 9

print(f'{celsius} Celsius is equal {round(fahrenheit,2)} Fahrenheit')
