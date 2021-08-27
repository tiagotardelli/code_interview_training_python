# code_interview_training_python
Sharpening the Axe

## Configurando o Ambiente
- Criando .venv (ambinete virtual do python)
    ```python
    python -m venv .venv #criando com a versão global do python
    python3 -m venv .venv #criando com a versão 3 do python3 Linux
    py -3 -m venv .venv #criando com a versão 3 do python3 Windows
    ```


## Comandos / Ferramentas Importantes
#### pip-tools
- Instalação do pip-tools (sugiro a instalação no global)
    ```python
    pip intall pip-tools
    ```
- Crie os arquivos requirements.in e requirement-dev.in para colocar em seus conteúdos o que é necessário para o projeto rodar, tanto na parte dev como com os para execução do código.
    - requeriments-dev.in
        ```txt
        -c requeriments.in
        pytest
        flake8
        ```
    
#### requeriments-dev.in
- flake8 = valida o código python com base na [PEP8](https://www.python.org/dev/peps/pep-0008/)
    - criar o arquivo .flake8 para configurar como será executado
        ```txt
        [flake8]
        max-line-length = 120
        exclude=.venv
        ``` 