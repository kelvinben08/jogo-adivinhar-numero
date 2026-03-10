"""
Jogo de Adivinhar o Número

Programa que gera um número aleatório entre 1 e 100 e permite que o usuário tente adivinhar.
Versão 1.0
"""
from random import randint

TITULO = "Jogo de Adivinhar o Número"
TAMANHO_LINHA = 78


def ler_palpite() -> int:
    """
    Solicita ao usuário um número entre 1 e 100, valida a entrada e retorna um palpite válido.
    """
    while True:
        try:
            numero = int(input("Digite um número entre 1 e 100: "))

            if 1 <= numero <= 100:
                return numero
            else:
                raise ValueError("Número fora do intervalo! Digite um número entre 1 e 100.")

        except ValueError as erro:
            print(f"Entrada inválida: {erro}")


def main():
    """
    Programa principal que executa o fluxo do programa.
    """
    print(TAMANHO_LINHA * "=")
    print(TITULO.center(TAMANHO_LINHA))
    print(TAMANHO_LINHA * "=")

    numero_secreto = randint(1, 100)
    palpite = 0

    while palpite != numero_secreto:
        palpite = ler_palpite()

        if palpite < numero_secreto:
            print("Muito baixo! Tente novamente.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente novamente.")
        else:
            print(f"Parabéns! Você acertou o número {numero_secreto}!")

        print(TAMANHO_LINHA * "=")


if __name__ == '__main__':
    main()
