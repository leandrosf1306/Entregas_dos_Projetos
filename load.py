# Definir novamente o mapeamento de tipos de dados para MySQL
type_mapping = {
    "int64": "INT",
    "float64": "FLOAT",
    "object": "TEXT",
    "datetime64[ns]": "DATETIME"
}

# Nome da tabela
table_name = "projetos"

# Gerar comando SQL para criação da tabela
create_table_sql = f"CREATE TABLE {table_name} (\n"

# Criar colunas com base nos tipos de dados do DataFrame
columns_sql = []
for col, dtype in df_cleaned.dtypes.items():
    sql_type = type_mapping.get(str(dtype), "TEXT")
    columns_sql.append(f"  `{col}` {sql_type}")

create_table_sql += ",\n".join(columns_sql) + "\n);"

# Corrigir a geração de valores para inserção no SQL
insert_sql = []
for _, row in df_cleaned.iterrows():
    values = []
    for val in row:
        if pd.isna(val):  # Se for NaN, inserir NULL
            values.append("NULL")
        elif isinstance(val, str):  # Se for string, escapar aspas simples corretamente
            values.append("'" + val.replace("'", "''") + "'")
        elif isinstance(val, pd.Timestamp):  # Se for data, formatar corretamente
            values.append("'" + val.strftime('%Y-%m-%d %H:%M:%S') + "'")
        else:  # Para números, manter o valor original
            values.append(str(val))
    insert_sql.append(f"INSERT INTO {table_name} VALUES ({', '.join(values)});")

# Juntar todos os comandos SQL
full_sql_script = create_table_sql + "\n\n" + "\n".join(insert_sql)

# Salvar o script SQL em um arquivo
sql_file_path = "/mnt/data/PS_Dados_Projetos.sql"
with open(sql_file_path, "w", encoding="utf-8") as f:
    f.write(full_sql_script)

# Retornar o caminho do arquivo SQL gerado
sql_file_path
