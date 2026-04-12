from src.calculator import (
    emissoes_eletricidade,
    emissoes_carro,
    emissoes_voo,
    emissoes_transporte_publico,
    emissoes_residuos,
    emissoes_dieta,
)
from src.input_handler import ler_float_positivo, ler_opcao
from src.report import mostrar_resumo
from src.storage import salvar_resultado_csv


def main():
    print("CALCULADORA DE CARBONO - Neutralidade Climática\n")

    kwh = ler_float_positivo("Consumo de eletricidade (kWh/ano): ")

    km_carro = ler_float_positivo("Quilometragem anual do carro (km): ")
    consumo_carro = ler_float_positivo("Consumo médio do carro (litros/100km): ")
    tipo_combustivel = ler_opcao(
        "Tipo de combustível (gasolina/diesel): ",
        ["gasolina", "diesel"]
    )

    km_voo = ler_float_positivo("Distância anual de voos (km): ")
    tipo_voo = ler_opcao(
        "Tipo de voo (curto/longo): ",
        ["curto", "longo"]
    )

    km_tp = ler_float_positivo("Distância anual de transporte público (km): ")
    modo_tp = ler_opcao(
        "Modo de transporte público (onibus/trem): ",
        ["onibus", "trem"]
    )

    kg_lixo = ler_float_positivo("Quantidade anual de resíduos (kg): ")
    tipo_dieta = ler_opcao(
        "Tipo de dieta (muita carne/mista/vegetariana): ",
        ["muita carne", "mista", "vegetariana"]
    )

    emissoes = {
        "Eletricidade": emissoes_eletricidade(kwh),
        "Carro": emissoes_carro(km_carro, consumo_carro, tipo_combustivel),
        "Voo": emissoes_voo(km_voo, tipo_voo),
        "Transporte Público": emissoes_transporte_publico(km_tp, modo_tp),
        "Resíduos": emissoes_residuos(kg_lixo),
        "Dieta": emissoes_dieta(tipo_dieta),
    }

    mostrar_resumo(emissoes)

    salvar = ler_opcao("Deseja salvar o resultado em CSV? (sim/nao): ", ["sim", "nao"])
    if salvar == "sim":
        salvar_resultado_csv(emissoes)
        print("Resultado salvo com sucesso em data/results.csv")


if __name__ == "__main__":
    main()