from src.calculator import (
    kg_para_toneladas,
    emissoes_eletricidade,
    emissoes_carro,
    emissoes_residuos,
)


def test_kg_para_toneladas():
    assert kg_para_toneladas(1000) == 1


def test_emissoes_eletricidade():
    assert emissoes_eletricidade(2000) == 950.0


def test_emissoes_carro_gasolina():
    resultado = emissoes_carro(12000, 8.33, "gasolina")
    esperado = (8.33 / 100) * 12000 * 2.31
    assert round(resultado, 2) == round(esperado, 2)


def test_emissoes_residuos():
    assert emissoes_residuos(600) == 120.0