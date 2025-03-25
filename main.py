import pandas as pd
import mysql.connector

# Configurações do banco de dados
DB_CONFIG = {
    'host': 'localhost',  # Altere se necessário
    'user': 'root',       # Substitua pelo seu usuário MySQL
    'password': 'senha',  # Substitua pela sua senha MySQL
    'database': 'projetos'
}

# Carregar os dados do Excel
df = pd.read_excel("PS_Dados_Projetos_Limpos.xlsx")

# Conectar ao MySQL
conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

# Criar a tabela (caso não exista)
cursor.execute("""
CREATE TABLE IF NOT EXISTS base_dados_projeto (
    item_id INT PRIMARY KEY,
    item_name VARCHAR(255),
    item_type VARCHAR(100),
    outcome_projection_value FLOAT,
    work_progress_value FLOAT,
    work_progress_expected_value FLOAT,
    target_date DATE,
    board VARCHAR(255),
    workflow VARCHAR(255),
    work_item VARCHAR(255),
    column_name VARCHAR(255),
    lane VARCHAR(255),
    block_count FLOAT,
    block_reason VARCHAR(255),
    block_time FLOAT,
    is_blocked VARCHAR(50),
    blocker_label VARCHAR(255),
    created_at DATETIME,
    custom_card_id FLOAT,
    cycle_time FLOAT,
    deadline DATE,
    end_date DATE,
    last_modified DATETIME,
    last_moved DATETIME,
    logged_time FLOAT,
    planned_end_date DATE,
    planned_start_date DATE,
    position_in_cell FLOAT,
    priority VARCHAR(50),
    section VARCHAR(255),
    size FLOAT,
    start_date DATE,
    stickers VARCHAR(255),
    tags VARCHAR(255),
    type FLOAT,
    workspace VARCHAR(255),
    Parent_ID INT,
    natureza_do_item TEXT,
    tempo_decorrido FLOAT,
    data_inicio_entrega DATE,
    data_fim_entrega DATE,
    quadro VARCHAR(255),
    secao VARCHAR(255)
);
""")

# Inserir os dados no MySQL
for _, row in df.iterrows():
    sql = """
    INSERT INTO base_dados_projeto VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = tuple(row.fillna(None))
    cursor.execute(sql, values)

# Commit e fechar conexão
conn.commit()
cursor.close()
conn.close()

print("Dados importados com sucesso!")
