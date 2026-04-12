import csv
import os
from datetime import datetime

from src.calculator import kg_para_toneladas, calcular_creditos, calcular_arvores


def salvar_resultado_csv(emissoes: dict[str, float], caminho_arquivo: str = "data/results.csv") -> None:
    os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)

    total_kg = sum(emissoes.values())
    total_ton = kg_para_toneladas(total_kg)
    creditos = calcular_creditos(total_kg)
    arvores = calcular_arvores(total_kg)

    arquivo_existe = os.path.isfile(caminho_arquivo)

    with open(caminho_arquivo, mode="a", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)

        if not arquivo_existe or os.path.getsize(caminho_arquivo) == 0:
            writer.writerow([
                "data",
                "eletricidade_kg",
                "carro_kg",
                "voo_kg",
                "transporte_publico_kg",
                "residuos_kg",
                "dieta_kg",
                "total_kg",
                "total_ton",
                "creditos",
                "arvores"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            emissoes.get("Eletricidade", 0),
            emissoes.get("Carro", 0),
            emissoes.get("Voo", 0),
            emissoes.get("Transporte Público", 0),
            emissoes.get("Resíduos", 0),
            emissoes.get("Dieta", 0),
            total_kg,
            total_ton,
            creditos,
            arvores
        ])