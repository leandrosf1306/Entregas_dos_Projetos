# Recarregar o arquivo para visualizar suas planilhas
xls = pd.ExcelFile("/mnt/data/PS_Dados_Projetos.xlsx")

# Listar os nomes das planilhas disponíveis
xls.sheet_names

# Carregar a planilha em um DataFrame
df = pd.read_excel(xls, sheet_name="base_dados_projeto")

# Exibir as primeiras linhas para análise
df.head()

# Remover duplicatas
df_cleaned = df.drop_duplicates()

# Remover colunas com muitos valores nulos (se mais de 50% dos valores forem nulos)
threshold = 0.5 * len(df_cleaned)
df_cleaned = df_cleaned.dropna(axis=1, thresh=threshold)

# Preencher valores nulos restantes de forma adequada
df_cleaned = df_cleaned.fillna({
    "item_id": 0,
    "item_name": "Desconhecido",
    "item_type": "Não especificado",
    "work_progress_value": 0,
    "work_progress_expected_value": 0,
    "target_date": "Data não informada",
    "board": "Não especificado",
    "workflow": "Não especificado",
    "work_item": "Não especificado"
})

# Converter tipos de dados
df_cleaned["item_id"] = df_cleaned["item_id"].astype(int)
df_cleaned["work_progress_value"] = df_cleaned["work_progress_value"].astype(float)
df_cleaned["work_progress_expected_value"] = df_cleaned["work_progress_expected_value"].astype(float)

# Converter colunas de data
date_columns = ["Data_inicio_entrega", "Data_Fim_Entrega"]
for col in date_columns:
    if col in df_cleaned.columns:
        df_cleaned[col] = pd.to_datetime(df_cleaned[col], errors='coerce')

# Exibir resumo dos dados após limpeza
df_cleaned.info()

