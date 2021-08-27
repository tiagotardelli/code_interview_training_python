# def funcao():
#     print('dentro da funcao')
#
# funcao()

# def funcao(nome):
#     print('Bom dia, ' + nome)
#
# funcao('Tiago!')
# funcao('Enrico')
#     funcao('Vanessa')

# def funcao(nome1, nome2, nome3):
#     print(nome1 + ', ' + nome2 + ', ' + nome3)
#
# funcao('Tiago', 'Enrico', 'Vanessa')
# funcao('Naruto', 'Sasuke', 'Sakura')
# funcao('Inuyasha', 'Kagome', 'Miroku')

# def funcao(pais = 'Brasil'):
#     return  pais
#
# argentina = funcao('Argentina')
# brasil = funcao()
# chile = funcao('Chile')
#
# print(argentina, brasil, chile)


def summation(num):
    total = 0
    print(num)
    print(range(num+1))
    for seq in range(num+1):
        print(seq)
        total = total + seq
        print(total)
    return total


print(summation(1))
