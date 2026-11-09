# 🐍 Estudos de Python

Repositório dedicado ao estudo progressivo de **Python, lógica de programação, automação e desenvolvimento de pequenos projetos**.

A proposta é registrar a evolução prática dos estudos de forma organizada, mantendo cada módulo simples, documentado e fácil de expandir.

## Conteúdo implementado

- `fundamentals/hello_cs50.py`: saudação com normalização de espaços, validação de nome e separação entre função e terminal.
- `tests/test_hello_cs50.py`: testes com a biblioteca padrão.
- GitHub Actions executa os testes em Python 3.10, 3.12 e 3.13.
- As pastas `automation/` e `projects/` ainda são roteiros de estudo, sem implementações.

Requer Python 3.10+ e não precisa instalar dependências. Na raiz:

```bash
python -m fundamentals.hello_cs50
python -m unittest discover -s tests -v
```

## 📚 Organização

### [fundamentals/](./fundamentals)
Base da linguagem Python: sintaxe, tipos de dados, condicionais, loops, funções, coleções e tratamento de exceções.

### [automation/](./automation)
Estudos de automação, manipulação de arquivos, processamento de dados, scripts utilitários e integração com ferramentas e APIs.

### [projects/](./projects)
Pequenos projetos práticos para aplicar os conceitos estudados e desenvolver código mais modular e reutilizável.

## 🎯 Objetivos de aprendizagem

- fortalecer lógica de programação;
- desenvolver fluência em Python;
- praticar código limpo e modular;
- aprender a validar entradas e tratar erros;
- transformar exercícios em pequenos projetos;
- construir uma base para estudos posteriores de Engenharia de Software.

## 🛠️ Padrões do repositório

Conforme os módulos evoluírem, os estudos poderão incorporar:

- testes automatizados;
- documentação técnica;
- type hints;
- organização por módulos;
- integração contínua quando houver código que justifique CI.

O repositório não pretende apresentar exercícios simples como sistemas de produção. A documentação deve acompanhar apenas o que estiver realmente implementado.

## 👩‍💻 Autora

**Marcella Bongiolo**

Repositório pessoal de estudos e prática em Python.

## 📄 Licença

Distribuído sob a licença MIT.