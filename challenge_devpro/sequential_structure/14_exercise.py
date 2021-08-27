"""
João Papo-de-Pescador, a good man, bought a microcomputer to control the daily income of his work.
Every time he brings a weight of fish greater than that established by the fishing regulation of the state of
São Paulo (50 kilos) must pay a fine of R$ 4.00 per excess kilo. John needs you to make a program that
read the variable weight (weight of fish) and calculate the excess. Record in the excess variable the amount of kilos
in addition to the limit and in the variable fine the amount of the fine that João must pay. Print program data with
messages appropriate.
########################################################################################################################
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de
São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que
leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do
limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens
adequadas.
"""
REGULATION_WEIGHT = 50.00
FINE_KILO = 4.00

excess_weight = 0.00
amount_pay = 0.00

weight_fish = float(input('Enter the weight of fish: '))
if weight_fish > REGULATION_WEIGHT:
    excess_weight = weight_fish - REGULATION_WEIGHT
    amount_pay = excess_weight * FINE_KILO

    print(f'Your fish weight excess {round(excess_weight,2)} kilos, your fine amount to pay is ${round(amount_pay,2)}')
