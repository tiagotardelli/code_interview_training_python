''''
>>> sexo = 'M'
>>> if sexo.upper() == 'M':
...     print('Masculino')
... elif sexo/upper == 'F':
...     print('Feminino')
... else:
...     print('Sexo Inválido')
Masculino
'''

sexo = input("Digite o seu sexo. M - Masculino, F - Feminino: ")

if sexo.upper() == 'M':
    print('Masculino')
elif sexo.upper() == 'F':
    print('Feminino')
else:
    print('Sexo Inválido')

if __name__ == "__main__":
    import doctest
    doctest.testmod()
