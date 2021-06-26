"""
Make a Program that asks for the 4 bimonthly grades and shows the average.

Pt-br > Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

grade_1 = int(input('Enter first grade: '))
grade_2 = int(input('Enter second grade: '))
grade_3 = int(input('Enter third grade: '))
grade_4 = int(input('Enter fourth grade: '))

average = (grade_1+grade_2+grade_3+grade_4)/4

print(f'The avarage is: {average}')