from src.calculator import kg_para_toneladas, calcular_creditos, calcular_arvores


def mostrar_resumo(emissoes: dict[str, float]) -> float:
    total = sum(emissoes.values())

    print("\n===== RESULTADO FINAL =====")
    for categoria, valor in emissoes.items():
        porcentagem = (valor / total * 100) if total > 0 else 0
        print(f"{categoria:25s}: {valor:8.2f} kgCO2e ({porcentagem:5.2f}%)")

    print(f"\nTOTAL ANUAL ESTIMADO: {total:.2f} kgCO2e ({kg_para_toneladas(total):.2f} tCO2e)")
    print(f"CRÉDITOS NECESSÁRIOS: {calcular_creditos(total):.2f}")
    print(f"ÁRVORES NECESSÁRIAS: {calcular_arvores(total)}")

    return total