dados = [
    {
        'nome': 'Tiago',
        'sobrenome': 'Tardelli',
        'telefone': {'residencial': '1111-1111', 'móvel': '9.9999-9999'},
        'ddd': 19
    },
    {
        'nome': 'Fausto',
        'sobrenome': 'mago',
        'telefone': {'residencial': '1111-1111', 'móvel': '9.9999-9999'},
        'ddd': 51
    },
]

nomes_completos = [f"{dado['nome']} {dado['sobrenome']}" for dado in dados]

tiago_telefone_residencial = [
   dado['telefone']['residencial'] for dado in dados if dado['nome'] == 'Eduardo'
][0]
