# def hero(bullets, dragons):
#     if bullets >= 2*dragons:
#         return True
#     else:
#         return False
#     return


# def reverse_words(s):
#     list = s.split()
#     list.reverse()
#     return ' '.join(list)
#
# print(reverse_words('Nós adoramos Python'))

# def calcular_media(list):
#     if len(list):
#         return sum(list)/len(list)
#     else:
#         return 0
#
# print(calcular_media([1,5]))

# numbers = [1,2,3]
#
# copia = [elemento for elemento in numbers]
# print(copia)
#
# double = [el*2 for el in numbers]
# print(double)
#
# maior_que_1 = [x for x in numbers id x  > 1]
# print(maior_que_1)

# carro = {'cor': 'vermelho', 'motor': 'v8'}
#
# print(carro)
# print(carro['cor'])
# print(carro['motor'])
#
# carro['cor'] = 'azul'
# print(carro)
# carros = [{'brand' : 'ford',
#         'color' : 'black',
#         'condition' : '3 days left',
#         'country' : 'usa',
#         'lot' : '167754311',
#         'mileage' : '26241.0',
#         'model' : 'STW',
#         'price' : '54000',
#         'state' : 'pennsylvania',
#         'title_status' : 'clean vehicle',
#         'vin' : '1ft7w3bt0hef02785',
#         'year' : '2017'},
#         {'brand' : 'fiat',
#         'color' : 'blue',
#         'condition' : '3 days left',
#         'country' : 'usa',
#         'lot' : '167754310',
#         'mileage' : '6241.0',
#         'model' : 'QWS',
#         'price' : '24000',
#         'state' : 'pennsylvania',
#         'title_status' : 'clean vehicle',
#         'vin': '1gt7w3bt0hef02785',
#         'year': '2005'}]
#
# print(len(carros))
#
# carros_ford = [carro for carro in carros if carro['brand'] == 'ford']
# print(len(carros_ford))
#
# precos = [carro['price'] for carro in carros]
# print(precos)
#
# anos = [carro['year'] for carro in carros]
# print(anos)
# anos.sort()
# print(anos)
