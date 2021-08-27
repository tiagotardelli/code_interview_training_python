"""
Make a Program that asks how much you earn per hour and the number of hours worked in the month. Calculate and show the
of your salary in that month, knowing that 11% is deducted for Income Tax, 8% for INSS and 5%
for the union, make a program that gives us:
    a) gross salary.
    b) how much it paid to the INSS.
    c) how much it paid to the union.
    d) the net salary.
    e) calculate discounts and net salary, as shown in the table below:
    + Gross Salary: $
    - Income Tax (11%): $
    - INSS (8%): $
    - Union (5%): $
    = Net Salary: $

Note: Gross Salary - Discounts = Net Salary.
########################################################################################################################
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
para o sindicato, faça um programa que nos dê:
    a) salário bruto.
    b) quanto pagou ao INSS.
    c) quanto pagou ao sindicato.
    d) o salário líquido.
    e) calcule os descontos e o salário líquido, conforme a tabela abaixo:
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

INCOME_TAX = 0.11
INSS = 0.08
UNION = 0.05

earn_per_hour = float(input('How much you earn per hour: '))
hours_worked = float(input('The number of hours worked in the month: '))

gross_salary = earn_per_hour * hours_worked
paid_income_tax = gross_salary * INCOME_TAX
paid_inss = gross_salary * INSS
paid_union = gross_salary * UNION
net_salary = gross_salary - (paid_income_tax + paid_inss + paid_union)

print("+ Gross Salary: $ ", gross_salary)
print("- Income Tax(11 %): $ ", paid_income_tax)
print("- INSS(8 %): $ ", paid_inss)
print("- Union(5 %): $ ", paid_union)
print("= Net Salary: $ ", net_salary)
