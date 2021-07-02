"""
Make a program for a paint shop. The program should ask for the size in square meters of the area to be painted.
Consider that the paint coverage is 1 liter for every 3 square meters and that the paint is sold in 18 cans
liters, which cost R$ 80.00. Inform the user of the quantities of paint cans to be purchased and the total price.
########################################################################################################################
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

ONE_LITER_PAINT = 3
CANS_LITERS = 18
CANS_PRIXE = 80.00

#square_meters = input('Enter the size in square meters of the area to be painted: ')
square_meters = 40
cans_painted = ONE_LITER_PAINT * CANS_LITERS

