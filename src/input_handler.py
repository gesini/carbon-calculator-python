def ler_float_positivo(mensagem: str) -> float:
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print("Digite um valor maior ou igual a zero.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def ler_opcao(mensagem: str, opcoes_validas: list[str]) -> str:
    while True:
        valor = input(mensagem).strip().lower()
        if valor in opcoes_validas:
            return valor
        print(f"Opção inválida. Escolha entre: {', '.join(opcoes_validas)}.")