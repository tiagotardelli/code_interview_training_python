"""
Make a Program that asks how much you earn per hour and the number of hours worked in the month. calculate and show your
total salary for that month.
########################################################################################################################
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e
mostre o total do seu salário no referido mês.
"""

earn_per_hour = float(input('How much you earn per hour: '))
hours_worked_month = float(input('How much hours you worked in the month: '))
total_salary_month = earn_per_hour * hours_worked_month
print(f'Your total salary for that month is {total_salary_month}')
