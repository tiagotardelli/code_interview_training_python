'''
Não aceita valores duplicados
 meu_dicionario = {
     "nome": "Rivon",
     "sobrenome": "L'mour Calcur",
     "idade": "30",
     "idade": "22"
 }

 print(meu_dicionario)
 print(meu_dicionario['nome'])

 meu_dicionario = {
     "marca": "Ford", # string
     "eletrico": False, #booleano
     "ano": 1964, #inteiro
     "cores": ["red", "white", "blue"] #lista
 }
 print(meu_dicionario)

 meu_dicionario = [{
     "nome": "Rivon",
     "sobrenome": "L'mour Calcur",
     "idade": 22
 },
 {
     "nome": "Tiago",
     "sobrenome": "Tardelli",
     "idade": 34
 }]

 #print(meu_dicionario.keys())
 print(meu_dicionario[0].values())

pesquisar em um dicionário
def get_drink_by_profession(param):
dictonary = { "Jabroni": "Patron Tequila",
            "School Counselor": "Anything with Alcohol",
             "Programmer": "Hipster Craft Beer",
             "Bike Gang Member": "Moonshine",
             "Politician": "Your tax dollars",
             "Rapper": "Cristal"}

 print(dictonary.get('farofa', 'Beer'))

 meu_dicionario = {
     "nome": "Rivon",
     "sobrenome": "L'mour Calcur",
     "idade": 22
 }

 #padrão percorrer as chaves
 for chave in meu_dicionario:
     print(chave)
 #chaves
 for chave in meu_dicionario.keys():
     print(chave)
 #Valores das chaves
 for chave in meu_dicionario.values():
     print(chave)

 for chave, valor in meu_dicionario.items():
    print(chave, valor)
 def compras_frutas(dictonary):
     array = []

     for chave, valor in dictonary.items():
         if valor["quantidade"] < 7 and valor["preco"] < 7:
             array.append({str(chave) : valor["quantidade"]})
     return array

 frutas = {
     "melancia": {"quantidade": 4, "preco": 10},
     "pera": {"quantidade": 2, "preco": 3},
     "uva": {"quantidade": 8, "preco": 8},
     "ameixa": {"quantidade": 5, "preco": 2},
     "abacaxi": {"quantidade" :15, "preco": 4},
     "banana": {"quantidade": 6, "preco": 4}
 }

 compras = compras_frutas(frutas)
 print(compras)

'''

initialize = {
    "display": {"width": 600, "height": 400},
    "game_name": "Meu jogo",
    "colors": {"red": (219, 31, 31), "green": (44, 219, 31)},
    "square_size": 200,
    "circule_radius": 10,
    "initial_position": {"x": 200, "y": 100}
}
'''Definindo o tamanho da tela para pygame'''
print(initialize.get("display").get("width"))
