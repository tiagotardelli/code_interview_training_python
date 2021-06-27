## Conteúdo retirado do canal do "Eduardo Mendes" - https://www.youtube.com/watch?v=NtZY3AmsBSk 
# Primitive obssesion
- A obsessão por primitivos é caracterizada por estuturas que podem ser representadas por objetos concretos, mas ela é 
  representada por um tipo "primtivo" da linguagem. Como o nosso dicionário.
- Quando não respeitamos uma regra e domínios, acabamos fazendo funções ou rotinas "soltas" para conseguir obter o 
  resultado esperado.
- Representar algo complexo usando a estutura mais simples da linguagem

# NamedTuple & typing.NamedTuple
### Importante
- Declarar com a primeira letra do nome em maiúscula, exemplo "Usuario" 
### Vantages
- Para tentar fugir da "dificuldade" de acesso, temos as nametuples, que são "costrutoras" de objetos.
- Explorando as namedtuples
    - Imutabilidade
        - Não recebe novas atribuições para valores
        - Tem o mesmo estado até o final da execução
    - Representação
        - Já implementa \_\_repr__ e \_\_str__
    - É comparável
        - Implementa \_\_eq__
    - É montada de maneira programática
        - namedtuple('nome', *args)
- Se precirar de tipagem uso o typing.NamedTuple (PEP-526)
    - Caso você queira uma checagem estática de tipos, você pode implementar NamedTuple tipada.
    - Pode-se uma **mypy** para checagem das typagens
### Desvantagens
- Imutabilidade
    - Pode ser que você não queira.
- Extensão
    - Não é possível estender tuplas (herança).
- A representação do objeto é sempre completa.
- Não é possível criar métodos.

# Como fugir da primitive obssesion
- Existe um pattern chamado _**Value Object**_, que tem como ideia criar uma classe para representar o domínio. Ou seja, 
  decemos criar um objeto para representar uma abstração.
### Vantages
- Mutabilidade / Imutabilidade
    - Vai ao seu gosto
- Expansão
    - Podemos usar herança
- Métodos
    - Podemos criar métodos
### Desvantagens
- A implementação simplória é cara. Para ter a mesma funcionalidade que uma NamedTuple:
    - Precisa implementar \_\_eq__ e \_\_repr__

# dataclasses
- PEP-557
    - "mutable namedtuples with defaults (...) which inspects a class definition
      for variables with type annotations"
      ###### "namedtuples mutáveis com valores default que inspecionam a definição classe para variáveis com anotações 
      ###### de tipo"
    - As dataclasses foram feitas para facilitar objetos de domínio específico. Elas implementam a representação, a 
      mutabilidade ou imutabilidade, a comparaçao e o hash das classes. Assim, sendo mais simples de implementar a 
      preço de um decorador. Por serem classes, podem herdar outras classes e também criar métodos customizados.
    - A ideia do post_init é ser executado aapós a inicilização da classe.
        - Definimos um valor default (None) e preenchemos após a inicialização
    - O decorador diz o que esperamos dessa classe, o que faz ela ser totalmente customizável:
        - init=False
            - se quisermos que a classe não inicie
        - repl=False
            - Se não quisermos a representação da classe
        - rq=False
            - Se não quisermos a comparação
        - frozem=False
            - Se não quisermos que seja mutável
    - A função field
        - Nos auxilia nas escolhas e o qe fazer com os atributos. Vai ser carregado depois? Tem um valor padrão? Se for
        vazio, posso fazer um factory? Devo exibir esse dado na representação?

# Alternativa a dataclass - não bultin
- Attrs
    - Biblioteca mais antiga e com mais funções
    - Funciona com typing e sem typinig
    - "Classes sem boilerplate" (sem fazer, por exemplo: \_\_eq__ , \_\_init__ )
    - Possui validadores
    - É rápida
- Pydantic
    - Biblioteca mais "nova"
    - Só aceita typing
    - Padrão no fastAPI
    - Possui validadores
    
# Comparação rápida
|      Features      | dataclass | Attrs | Pydantic |
|--------------------|:---------:|:------:|--------:|
|       Frozen       |     X     |    X   |    X    |
|      Defaults      |     X     |    X   |    X    |
|      To tuple      |     X     |    X   |    X    |
|       To dict      |     X     |    X   |    X    |
|     Validators     |           |    X   |    X    |
|     Converters     |           |    X   |    X    |
|        slots       |           |    X   |         |
|Criação Programática|     X     |    X   |    X    |