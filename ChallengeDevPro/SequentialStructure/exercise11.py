"""
Make a Program that asks for 2 integers and a real number. Calculate and show:
    a) the product of the double of the first with half of the second.
    b) the sum of the triple of the first and the third.
    c) the third to the cube.
########################################################################################################################
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    a) produto do dobro do primeiro com metade do segundo .
    b) soma do triplo do primeiro com o terceiro.
    c) terceiro elevado ao cubo.
"""

integer_1 = int(input('Enter a first integer: '))
integer_2 = int(input('Enter a second integer: '))
real_number = float(input('Enter a real number: '))

print('The product of the double of the first with half the second: ', (integer_1*2) * (integer_2/2))
print('The sum of the triple of the first and the third: ', (integer_1*3) + real_number)
print('The third to the cube', real_number**3)