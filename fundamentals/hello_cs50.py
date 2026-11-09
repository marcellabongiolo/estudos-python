"""Exercício introdutório: validação, função reutilizável e entrada pelo terminal."""


def saudar(nome: str) -> str:
    """Retorna uma saudação para um nome não vazio."""
    if not isinstance(nome, str):
        raise TypeError("O nome deve ser uma string.")
    nome_limpo = " ".join(nome.split())
    if not nome_limpo:
        raise ValueError("Informe um nome.")
    return f"Olá, {nome_limpo}!"


def main() -> None:
    try:
        print(saudar(input("Qual é o seu nome? ")))
    except ValueError as erro:
        print(erro)


if __name__ == "__main__":
    main()
