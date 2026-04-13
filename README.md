# 🌱 Carbon Footprint Calculator (Python)

Uma calculadora de pegada de carbono desenvolvida em Python que estima emissões anuais de CO₂e com base em hábitos do usuário.

---

## 📌 Sobre o projeto

Este projeto foi desenvolvido como parte de uma Atividade Prática Supervisionada (APS) com foco em sustentabilidade e conscientização ambiental.

A aplicação permite calcular o impacto ambiental anual de uma pessoa considerando diferentes aspectos do dia a dia.

---

## ⚙️ Funcionalidades

- 🔌 Emissões por consumo de energia elétrica
- 🚗 Emissões por uso de carro
- ✈️ Emissões por viagens aéreas
- 🚌 Emissões por transporte público
- 🗑️ Emissões por resíduos
- 🥗 Emissões baseadas na dieta
- 📊 Cálculo total em kg e toneladas de CO₂e
- 🌳 Estimativa de árvores necessárias para compensação
- 💳 Estimativa de créditos de carbono
- 💾 Exportação dos resultados em CSV
- 🧪 Testes automatizados com pytest

---

## 🗂️ Estrutura do projeto


carbon-calculator-python/
├── src/
│ ├── calculator.py
│ ├── factors.py
│ ├── input_handler.py
│ ├── report.py
│ └── storage.py
├── tests/
├── data/
├── docs/
├── assets/
├── main.py
├── requirements.txt
├── README.md


---

## 🚀 Como executar o projeto

### 1. Instalar dependências

```bash
python -m pip install -r requirements.txt
2. Executar o programa
python main.py
🧪 Executar testes
python -m pytest
💡 Exemplo de uso
Consumo de eletricidade (kWh/ano): 2000
Quilometragem anual do carro (km): 12000
Consumo médio do carro (litros/100km): 8.33
Tipo de combustível: gasolina
Distância anual de voos (km): 0
Tipo de voo: curto
Distância anual de transporte público (km): 0
Modo: onibus
Quantidade de resíduos (kg): 600
Tipo de dieta: mista
🌍 Tecnologias utilizadas
Python 3
Pytest
CSV (armazenamento de dados)
📈 Possíveis melhorias
Interface gráfica (GUI)
Aplicação web com Streamlit
Dashboard com gráficos
Integração com banco de dados
Atualização dinâmica de fatores de emissão
🎯 Objetivo acadêmico

Este projeto tem como objetivo aplicar conceitos de programação, modularização, validação de dados e testes automatizados, além de promover consciência ambiental através da tecnologia.

👨‍💻 Autor

Desenvolvido por estudante de Ciência da Computação. 
