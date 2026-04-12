from src.factors import EMISSION_FACTORS


def kg_para_toneladas(kg: float) -> float:
    return kg / 1000


def emissoes_eletricidade(kwh: float) -> float:
    return kwh * EMISSION_FACTORS["eletricidade"]


def emissoes_carro(km: float, consumo_litros_100km: float, tipo_combustivel: str) -> float:
    litros = (consumo_litros_100km / 100) * km

    if tipo_combustivel == "gasolina":
        fator = EMISSION_FACTORS["gasolina"]
    elif tipo_combustivel == "diesel":
        fator = EMISSION_FACTORS["diesel"]
    else:
        raise ValueError("Tipo de combustível inválido.")

    return litros * fator


def emissoes_voo(km: float, tipo_voo: str) -> float:
    if tipo_voo == "curto":
        fator = EMISSION_FACTORS["voos_curto"]
    elif tipo_voo == "longo":
        fator = EMISSION_FACTORS["voos_longos"]
    else:
        raise ValueError("Tipo de voo inválido.")

    return km * fator


def emissoes_transporte_publico(km: float, modo: str) -> float:
    if modo == "onibus":
        fator = EMISSION_FACTORS["onibus"]
    elif modo == "trem":
        fator = EMISSION_FACTORS["trem"]
    else:
        raise ValueError("Modo inválido.")

    return km * fator


def emissoes_residuos(kg_lixo: float) -> float:
    return kg_lixo * EMISSION_FACTORS["desperdicio"]


def emissoes_dieta(tipo_dieta: str) -> float:
    if tipo_dieta == "muita carne":
        return EMISSION_FACTORS["dieta_rica_em_carne"]
    elif tipo_dieta == "mista":
        return EMISSION_FACTORS["dieta_mista"]
    elif tipo_dieta == "vegetariana":
        return EMISSION_FACTORS["dieta_vegetariana"]
    else:
        raise ValueError("Tipo de dieta inválido.")


def calcular_creditos(total_kg: float) -> float:
    return kg_para_toneladas(total_kg)


def calcular_arvores(total_kg: float) -> int:
    return round(total_kg / 22)