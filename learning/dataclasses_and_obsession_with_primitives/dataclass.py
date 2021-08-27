from typing import Dict
from dataclasses import dataclass, field, asdict, astuple


@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
# repr=False -> não tenho mais a representacão do valor
# frozen=True -> não aceita alteração dos valores após iniciado
class Pessoa:
    nome: str
    sobrenome: str
    ddd: int = field(repr=False)  # Quando representar a classe o DDD não vai aparecer, pois não tem representação
    telefone: Dict[str, str] = field(default_factory=dict)  # Se eu não passar nada o default é um dict vazio
    # nome_completo: str = None
    nome_completo: str = field(init=False)  # Não vou inicializar ele nesse momento

# Roda somente uma vez
    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'


if __name__ == '__main__':
    tiago_1 = Pessoa('Tiago', 'Tardelli', 19, {'residencial': '1', 'móvel': '2'})
    tiago_2 = Pessoa('Tiago', 'Tardelli', 19, {'residencial': '1', 'móvel': '2'})
    print(tiago_1.nome)  # 'Tiago'
    print(tiago_1 == tiago_2)  # True
    print(tiago_1)  # Pessoa(nome='Tiago', sobrenome='Tardelli', telefone={'residencial': 1, 'móvel': 2}, ddd=19, )
    # nome_completo='Tiago Tardelli'
    print(tiago_1.ddd)  # 19
    tiago_1.ddd = 40
    print(tiago_1.ddd)  # 40
    p = Pessoa('Carlos', 'Silva', 13)
    p.telefone |= {'móvel': '99'}
    print(p)
    p2 = Pessoa('Fabio', 'Carlos', 14)
    print(type(p2))
    p3 = asdict(p2)
    print(type(p3))
    p4 = astuple(p2)
    print(type(p4))
    p5 = Pessoa(nome='Silvia', sobrenome='Xaxin', ddd=19)
    pt = astuple(p5)
    print(pt)
    Pessoa(*pt[:-1])
    pd = (asdict(p5))
    print(pd)
''''del pd['nome_completo'] >>> Pessoa(**pd)'''
