from typing import Dict


class Pessoa:
    def __init__(self, nome: str, sobrenome: str, telefone: Dict[str, str], ddd: int):
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefone = telefone
        self.ddd = ddd

    def __eq__(self, other):
        return all([
            self.nome == other.nome,
            self.sobrenome == other.sobrenome,
            self.telefone == other.telefone,
            self.ddd == other.ddd
        ])

    def __repr__(self):
        return f'Pessoa{self.nome}, {self.sobrenome}, {self.telefone}, {self.ddd}'


tiago_1 = Pessoa('Tiago', 12, {'residencial': '1111-1111', 'móvel': '99999-9999'}, 19)
tiago_2 = Pessoa('Tiago', 13, {'residencial': '1111-1111', 'móvel': '99999-9999'}, 20)
