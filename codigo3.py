import json

# Exemplo de JSON com faturamento diário
dados_faturamento = """
{
  "faturamento_diario": [
    {"dia": 1, "valor": 1000.0},
    {"dia": 2, "valor": 2000.0},
    {"dia": 3, "valor": 0.0},
    {"dia": 4, "valor": 3000.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 4000.0},
    {"dia": 7, "valor": 5000.0},
    {"dia": 8, "valor": 6000.0},
    {"dia": 9, "valor": 0.0},
    {"dia": 10, "valor": 7000.0}
  ]
}
"""

# Parse do JSON
faturamento = json.loads(dados_faturamento)

# Filtrando apenas os dias com faturamento maior que 0
valores_validos = [dia["valor"] for dia in faturamento["faturamento_diario"] if dia["valor"] > 0]

# Calculando menor e maior valor de faturamento
menor_faturamento = min(valores_validos)
maior_faturamento = max(valores_validos)

# Calculando a média mensal (considerando apenas os dias com faturamento)
media_mensal = sum(valores_validos) / len(valores_validos)

# Contando os dias com faturamento superior à média
dias_acima_da_media = sum(1 for valor in valores_validos if valor > media_mensal)

# Resultados
print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento superior à média: {dias_acima_da_media}")
