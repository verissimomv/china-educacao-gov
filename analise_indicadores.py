"""
Análise SQL + Python dos Indicadores Educacionais da China
Lê o arquivo indicadores_educacao_china.csv, estrutura um banco SQLite,
executa consultas analíticas em SQL e gera resumo estatístico com pandas.
"""

import re
import sqlite3
import pandas as pd


def limpar_valor_numerico(valor_str: str):
    """Converte strings como '280,40', '>90' ou '13.360' em float para análise SQL."""
    texto = str(valor_str).strip()
    if "º" in texto:
        return None
    texto = texto.replace(">", "").replace("<", "")
    # Trata milhar com ponto (ex: 13.360) vs decimal com vírgula (ex: 280,40)
    if re.match(r"^\d{1,3}(\.\d{3})+$", texto):
        texto = texto.replace(".", "")
    else:
        texto = texto.replace(",", ".")
    try:
        return float(texto)
    except ValueError:
        return None


def main():
    # 1. Carregar CSV e preparar coluna numérica limpa
    df = pd.read_csv("indicadores_educacao_china.csv", encoding="utf-8-sig")
    df["valor_numerico"] = df["Valor"].apply(limpar_valor_numerico)
    df = df.rename(columns={
        "Categoria": "categoria",
        "Indicador": "indicador",
        "Valor": "valor_texto",
        "Unidade": "unidade",
        "Ano_Referencia": "ano_referencia",
        "Recorte_Regional": "recorte_regional",
        "Observacoes": "observacoes"
    })

    # 2. Criar banco SQLite local (educacao_china.db)
    conn = sqlite3.connect("educacao_china.db")
    df.to_sql("indicadores_educacao_china", conn, if_exists="replace", index=False)

    # 3. Executar consultas SQL
    queries = {
        "Distribuição por Categoria": """
            SELECT categoria, COUNT(*) AS qtd_indicadores
            FROM indicadores_educacao_china
            GROUP BY categoria
            ORDER BY qtd_indicadores DESC;
        """,
        "Evolução Histórica (1982-2020)": """
            SELECT
                ano_referencia AS ano,
                MAX(CASE WHEN indicador LIKE 'Anos médios de escolaridade%' THEN valor_numerico END) AS escolaridade_media_anos,
                MAX(CASE WHEN indicador LIKE 'Taxa de analfabetismo (%' THEN valor_numerico END) AS analfabetismo_pct
            FROM indicadores_educacao_china
            WHERE categoria = 'Evolução Histórica'
              AND (indicador LIKE 'Anos médios%' OR indicador LIKE 'Taxa de analfabetismo (%')
            GROUP BY ano_referencia
            ORDER BY ano_referencia ASC;
        """,
        "Desempenho PISA 2025 (B-S-J-Z)": """
            SELECT indicador, valor_numerico AS pontos, observacoes
            FROM indicadores_educacao_china
            WHERE categoria = 'Desempenho Internacional (PISA)'
              AND ano_referencia = '2025'
            ORDER BY valor_numerico DESC;
        """,
        "Assimetrias Regionais (Censo 2020)": """
            SELECT recorte_regional, indicador, valor_numerico, unidade
            FROM indicadores_educacao_china
            WHERE categoria = 'Desigualdades Regionais (Censo 2020)'
            ORDER BY recorte_regional;
        """
    }

    for titulo, sql in queries.items():
        print(f"\n=== {titulo} ===")
        resultado = pd.read_sql_query(sql, conn)
        print(resultado.to_string(index=False))

    conn.close()


if __name__ == "__main__":
    main()
