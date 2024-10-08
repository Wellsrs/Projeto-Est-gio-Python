# Dicionário com o faturamento de cada estado
faturamento_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcular o valor total do faturamento
faturamento_total = sum(faturamento_por_estado.values())

# Calcular e exibir o percentual de cada estado
print("Percentual de representação por estado:\n")
for estado, valor in faturamento_por_estado.items():
    percentual = (valor / faturamento_total) * 100
    print(f"{estado}: {percentual:.2f}%")
