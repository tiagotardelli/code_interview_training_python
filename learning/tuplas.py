# tupla = (1, 2, 3)
# print(tupla[0])
#
# lista = [1, 2, 3]
# print(lista)
# lista[0] = 100
# print(lista)
#
# ##Da erro, não pode atribuir valor para tupla
# ##tupla[0] = 100
#
# #tem que ter a vírgula no final, se não o interpretador acha que é string
# tupla2 = ('ola',)
# tupla2 = ('ola', 'fui')
# string_ola, string_fui = tupla2
# print(tupla2)
#
# favorite_animal = ("sloth", )
# print(type(favorite_animal))
# print(favorite_animal)
#
# animals = ("dog", "cat", "squirrel")
# print(animals[0])
# print(animals[1:])
#
# lista_teste = ["joão", "maria"]
# tupla_teste = (lista_teste, )
# print(tupla_teste)
# lista_teste = ["glauber"]
# print(lista_teste)
# tupla_teste = lista_teste,
# print(tupla_teste)
#
# my_list = []
# for i in range(10):
#     my_list.append(i)
# print(my_list)
#
# my_tuple = ()
# for i in range(10):
#     my_tuple +=(i,)
#
# tupla_nova = (11, 33, 42, 50, 33, 98, 33)
# #qunatidade de ocorrências do valor
# print(tupla_nova.count(33))
# #primeira ocorrência do valor
# print(tupla_nova.index(33))

a = (1, 2, 3, 4,)
b = ('a', 3, 1, 't',)
c = a + b
print(c)
