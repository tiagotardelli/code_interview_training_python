'''
    - NamedTuple, porém tipada
'''

from typing import NamedTuple, Dict

class Pessoa(NamedTuple):
    nome: str
    sobrenome: str
    telefone: Dict[str,str]
    ddd: int

tiago = Pessoa('Tiago', 8, {'residencial': '1111-1111', 'móvel': '99999-9999'}, 20)