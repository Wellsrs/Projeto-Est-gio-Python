import json

# Função para carregar os dados de faturamento a partir de um arquivo JSON
def carregar_dados_faturamento(arquivo):
    with open(arquivo, 'r') as file:
        dados = json.load(file)
    return dados

# Função para calcular o menor, maior faturamento e dias com faturamento acima da média
def calcular_faturamento(dados_faturamento):
    valores = [dia['valor'] for dia in dados_faturamento if dia['valor'] > 0]  # Ignorar dias sem faturamento
    
    if not valores:  # Caso não haja valores válidos
        return None, None, 0
    
    menor_faturamento = min(valores)
    maior_faturamento = max(valores)
    media_mensal = sum(valores) / len(valores)
    
    dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media

# Carregar o JSON com os dados de faturamento
arquivo_json = 'faturamento.json'  # Substitua pelo caminho do seu arquivo
dados_faturamento = carregar_dados_faturamento(arquivo_json)

# Calcular os resultados
menor, maior, dias_acima_media = calcular_faturamento(dados_faturamento)

# Exibir os resultados
print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
