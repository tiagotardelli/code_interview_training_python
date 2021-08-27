from collections import namedtuple

pessoa = namedtuple('Pessoa', 'nome sobrenome telefone ddd')

dados = [
    pessoa('Tiago', 'Tardelli', {'residencial': '1111-1111', 'móvel': '99999-9999'}, 19),
    pessoa('Carlo', 'Silva', {'residencial': '1111-1111', 'móvel': '99999-9999'}, 50)
]

tiago = dados[0]  # OU
tiago = pessoa('Tiago', 'Tardelli', {'residencial': '1111-1111', 'móvel': '99999-9999'}, 19)

tiago.nome  # 'Tiago'
tiago.sobrenome  # 'Tardelli'
tiago[0]  # 'Tiago'

for item in tiago:
    print(item)
