-- ============================================================================
-- SCHEMA E CONSULTAS ANALÍTICAS: INDICADORES EDUCACIONAIS DA CHINA
-- Compatível com SQLite, PostgreSQL e MySQL
-- ============================================================================

DROP TABLE IF EXISTS indicadores_educacao_china;

CREATE TABLE indicadores_educacao_china (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    categoria VARCHAR(100) NOT NULL,
    indicador VARCHAR(255) NOT NULL,
    valor_texto VARCHAR(50) NOT NULL,
    valor_numerico DECIMAL(10, 2),
    unidade VARCHAR(60) NOT NULL,
    ano_referencia VARCHAR(30) NOT NULL,
    recorte_regional VARCHAR(120) NOT NULL,
    observacoes TEXT
);

-- 1. Contagem de indicadores por categoria e recorte regional
SELECT 
    categoria,
    COUNT(*) AS total_indicadores,
    COUNT(DISTINCT recorte_regional) AS recortes_distintos
FROM indicadores_educacao_china
GROUP BY categoria
ORDER BY total_indicadores DESC;

-- 2. Evolução histórica da escolaridade média e analfabetismo (1982-2020)
SELECT 
    ano_referencia,
    MAX(CASE WHEN indicador LIKE 'Anos médios de escolaridade%' THEN valor_numerico END) AS anos_escolaridade,
    MAX(CASE WHEN indicador LIKE 'Taxa de analfabetismo (%' THEN valor_numerico END) AS taxa_analfabetismo_pct
FROM indicadores_educacao_china
WHERE categoria = 'Evolução Histórica'
  AND (indicador LIKE 'Anos médios%' OR indicador LIKE 'Taxa de analfabetismo (%')
GROUP BY ano_referencia
ORDER BY ano_referencia ASC;

-- 3. Comparativo PISA 2025 (Grupo B-S-J-Z) ordenado por pontuação
SELECT 
    indicador,
    valor_numerico AS pontuacao_china,
    observacoes
FROM indicadores_educacao_china
WHERE categoria = 'Desempenho Internacional (PISA)'
  AND ano_referencia = '2025'
ORDER BY valor_numerico DESC;

-- 4. Assimetrias Regionais (Leste vs. Oeste no Censo 2020)
SELECT 
    recorte_regional,
    indicador,
    valor_numerico,
    unidade,
    observacoes
FROM indicadores_educacao_china
WHERE categoria = 'Desigualdades Regionais (Censo 2020)'
ORDER BY recorte_regional, indicador;
