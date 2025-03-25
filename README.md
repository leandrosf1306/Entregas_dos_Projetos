# ETL - Extração de Dados via API (Entregas_dos_Projetos)

## Descrição
Este projeto implementa um pipeline ETL (Extract, Transform, Load) que extrai dados de uma API, transforma-os conforme a necessidade e carrega os dados processados em um banco de dados.

## Tecnologias Utilizadas
- Glue AWS
- Python 3.x
- Pandas
- Requests
- OpenPyXL
- SQLAlchemy
- MySQL

## Estrutura do Projeto
```
.
├── data/                   # Pasta para armazenar arquivos Excel
├── scripts/                # Scripts ETL
│   ├── extract.py          # Extração de dados (Conexão e ingestão via Glue)
│   ├── transform.py        # Transformação de dados
│   ├── load.py             # Carga de dados
│   └── main.py             # Execução do pipeline ETL
├── README.md               # Documentação

```

## Repositório:
   
   git clone https://github.com/leandrosf1306/Entregas_dos_Projetos.git
   cd Entregas_dos_Projetos
   

## Funcionalidades
### Extração (Extract)
- A API é acessada via requisições HTTP para coletar os dados.
- O arquivo Excel é lido utilizando a biblioteca Pandas.

### Transformação (Transform)
- Limpeza e padronização dos dados.
- Remoção de valores nulos e duplicados.
- Conversão de formatos e tipos de dados.

### Carga (Load)
- Armazena os dados tratados no banco de dados configurado.
