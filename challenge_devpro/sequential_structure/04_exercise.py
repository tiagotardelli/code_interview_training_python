"""
Make a Program that asks for the 4 bimonthly notes and shows the average.
########################################################################################################################
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

note_1 = input('Enter the first note: ')
note_2 = input('Enter the second note: ')
note_3 = input('Enter the third note: ')
note_4 = input('Enter the fourth note: ')

average = (note_1 + note_2 + note_3 + note_4) / 4
print(f'The bimonthly average is {average}')
