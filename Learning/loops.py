# carinho_compras = ['Leite', 'ovos', 'presunto', 'queijo', 'pão', 'café']
# for item in carinho_compras:
#     print(item)

# for letra in "Olá Mundo":
#     print(letra)

# found = False
# nums = [3, 4, 7, 2, 8, 4, 6]
#
# print(enumerate(nums))
# for i, num in enumerate(nums):
#     if i > 0 and num + nums[i-1] == 10:
#         found = True
# print(found)

# def posicoes_que_iniciam_com(lista, letra='a'):
#     result = []
#     for i, palavra in enumerate(lista):
#         if palavra.startswith(letra):
#             result.append(i)
#     return result
#
# nomes = ['abc', 'hua', 'aaa', 'asdfg', 'bnm']
# print(posicoes_que_iniciam_com(nomes))

# for i in range(10):
#     print(i)
#
# for i in range(1, 11):
#     print(i)

# # de quantos em quantos elementos vai acontecer a iteração no range
# for i in range(1, 11, 3):
#     print(i)


# tabuada_nove = []
#
# for i in range(1, 11):
#     tabuada_nove.append(9*i)
# print(tabuada_nove)


# def tabuada(n):
#     tabuada = []
#     for i in range(1, 11):
#         tabuada.append(n*i)
#     return tabuada
#
# print(tabuada(2))

i = 0
n = 5

soma = 0

while i < n:
    soma = soma + i
    i = i + 1
print(soma)



# countdown = 3
# while countdown > 0:
#     print(countdown, "...", sep="")
#     countdown -= 1
# print("Blast odd!")
