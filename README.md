# 🌱 Carbon Footprint Calculator (Python)

Uma calculadora de pegada de carbono desenvolvida em Python que estima emissões anuais de CO₂e com base em hábitos do usuário.

---

## 📌 Sobre o projeto

Este projeto foi desenvolvido como parte de uma Atividade Prática Supervisionada (APS) com foco em sustentabilidade e conscientização ambiental.

A aplicação calcula o impacto ambiental anual considerando diferentes aspectos do dia a dia.

---

## ⚙️ Funcionalidades

- 🔌 Emissões por consumo de energia elétrica  
- 🚗 Emissões por uso de carro  
- ✈️ Emissões por viagens aéreas  
- 🚌 Emissões por transporte público  
- 🗑️ Emissões por resíduos  
- 🥗 Emissões baseadas na dieta  
- 📊 Total anual em kg e toneladas de CO₂e  
- 🌳 Estimativa de árvores para compensação  
- 💳 Estimativa de créditos de carbono  
- 💾 Exportação de resultados em CSV  
- 🧪 Testes automatizados com pytest  

---


## 🗂️ Estrutura do projeto

```text
carbon-calculator-python/
├── src/
│   ├── calculator.py
│   ├── factors.py
│   ├── input_handler.py
│   ├── report.py
│   └── storage.py
├── tests/
│   └── test_calculator.py
├── data/
│   └── results.csv
├── docs/
├── assets/
├── main.py
├── requirements.txt
├── README.md

---

🚀 Como executar o projeto
1. Instalar dependências
python -m pip install -r requirements.txt

2. Executar o programa
python main.py

3. Executar testes
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
CSV

📈 Possíveis melhorias
Interface gráfica (GUI)
Aplicação web com Streamlit
Dashboard com gráficos
Integração com banco de dados

👨‍💻 Autor
Desenvolvido por estudante de Ciência da Computação.