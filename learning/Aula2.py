# def enviar_mensagems(qualidade)
#     print('Gui lê comentário')
#     if qualidade == 'piada boa':
#         print('O Gui deu risada')
#     else:
#         print('O Gui tenta ficar sério')
#
# enviar_mensagems('piada boa')
# enviar_mensagems('piada ok')

# def estado_do_gui(qualidade)
#     print('Gui lê comentário')
#     if qualidade == 'piada boa':
#         return 'rindo'
#     else:
#         return 'serio'
#
# meu_estado = estado_do_gui('piada boa')
# print(meu_estado)

# numeros = [1,2,3]
#
# print(numeros[0])
#
# futuros_devs = ['lucas', 'isabela', 'chris']
#
# print(futurxs_devs[0])
# print(futurxs_devs[1])
# print(futurxs_devs[2])
#
# mais_devs = ['joel', 'priscila', 'rhuan']
#
# todxs_xs_devs = futurxs_devs + mais_devs
# print(todxs_xs_devs)
# print(todxs_xs_devs[-1])

# devs = ['davi', 'gabriel', 'juliana', 'ana']
#
# print(devs[0] + ' sabe python')
# print(devs[-1] + ' sabe python')
#
# for dev in devs:
#     print(dev + ' manda bem no python')

# frutas = ['pera', 'maca', 'laranja']
#
# def encontra_fruta(f):
#     for fruta in frutas:
#         if fruta == f:
#             print('achei a fruta!')
#             return
#         else:
#             print('ainda estou procurando')
#     print('não achei')
#
# encontra_fruta('maca')
#
# numeros = [1,2,3] + [4,5,6]
# numeros.append(7)
# print(numeros)


def find_average(nums):
    tam = len(nums)

    soma = 0

    for numero in nums:
        soma = soma + numero
    return soma/tam if tam else 0


print(find_average([]))


def say_hello_from_kenzie():
    print("Hello from Kenzie")


say_hello_from_kenzie()
say_hello_from_kenzie()
say_hello_from_kenzie()
say_hello_from_kenzie()


def untar_forma():
    forma_untada = True
    return forma_untada


def mistura_ingredientes(ovo, leite, farinha, manteiga=""):
    massa = ovo + leite + farinha + manteiga
    if untar_forma():
        forma = massa
    return forma


def assar_bolo(forma_com_massa, temperatura):
    if temperatura == 180:
        forno = forma_com_massa
    return forno


ovo = "ovo"
leite = "leite"
farinha = "farinha"
manteiga = "manteiga"


# forma_com_massa = mistura_ingredientes("3", leite, farinha)
# assar_bolo(forma_com_massa)

def multipica(x, y):
    return x * y


resultado = multipica(2, 5)
print(resultado)


def valida_string(nome):
    if nome.islower():
        print("está minúsculo")
    else:
        print("não está tudo minúsculo")

    if nome.isupper():
        print("está maiúsculo")
    else:
        print("não está tudo maiúsculo")

    # if nome.find("a") == -1:
    #     print("a não existe na string")

    print(nome.find("tia"))

    # print(nome.split(","))
    print(nome.split())
    nome_separado = nome.split()
    print(".".join(nome_separado))


# valida_string("maria foi visitar sua tia")
valida_string("maria foi visitar sua tia")
