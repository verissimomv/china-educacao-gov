# Educação na China — Cultura, Jornada, Equidade e Dados

![Status](https://img.shields.io/badge/Status-Ativo-C8102E)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Vanilla-F7DF1E?logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-SQLite-003B57?logo=sqlite&logoColor=white)

Projeto apresentativo, analítico e interativo dedicado ao sistema educacional da China. O repositório reúne uma aplicação web responsiva, uma base estruturada de indicadores educacionais e scripts em SQL e Python para modelagem relacional e análise exploratória.

---

## Sumário

1. [Visão Geral](#1-visão-geral)
2. [Estrutura do Repositório](#2-estrutura-do-repositório)
3. [Componentes do Projeto](#3-componentes-do-projeto)
4. [Principais Resultados das Análises](#4-principais-resultados-das-análises)
5. [Como Executar Localmente](#5-como-executar-localmente)
6. [Publicação via GitHub Pages](#6-publicação-via-github-pages)
7. [Referências e Fontes dos Dados](#7-referências-e-fontes-dos-dados)

---

## 1. Visão Geral

O sistema educacional chinês é o maior do mundo em escala e combina uma base universal gratuita de nove anos com etapas posteriores altamente competitivas voltadas à formação científica, tecnológica e profissional. Este repositório documenta tanto a dimensão cultural e social desse modelo quanto os dados oficiais que retratam sua evolução histórica, seu desempenho em avaliações internacionais e suas assimetrias regionais.

---

## 2. Estrutura do Repositório

```text
educacao-china/
├── README.md                     # Documentação principal e guia de uso do repositório
├── index.html                    # Site apresentativo e interativo (HTML5, CSS3 e JS)
├── indicadores_educacao_china    # Base de dados com 43 indicadores educacionais (CSV)
├── schema_e_consultas.sql        # Modelagem DDL e consultas analíticas em SQL
└── analise_indicadores.py        # Pipeline ETL em Python + SQLite para análise dos dados
```

---

## 3. Componentes do Projeto

### 3.1. Aplicação Web (`index.html`)
Interface desenvolvida em arquivo único (`HTML5`, `CSS3` e `JavaScript` puro) com hub superior em vermelho e seção principal em fundo branco com tipografia em vermelho escuro para proporcionar leitura confortável:
* **Cultura & Valores:** Herança confuciana, prestígio social da figura docente e rotina escolar colaborativa.
* **Jornada Escolar Interativa:** Abas dinâmicas detalhando a Educação Infantil, os Anos Compulsórios (9 anos), o Ensino Médio/Técnico e o Ensino Superior.
* **Questões Sociais & Equidade:** Análise dos contrastes entre campo e cidade, o sistema de registro domiciliar (*Hukou*), a política de *Dupla Redução* (*Shuangjian*), a gratuidade básica e as cotas regionais.
* **Aba Exclusiva de Indicadores:** Painel interativo organizado em quatro sub-abas (*Escala & Acesso*, *Desempenho PISA 2025*, *Evolução & IDH* e *Assimetrias Regionais*).

### 3.2. Base de Dados (`indicadores_educacao_china`)
Conjunto estruturado com **43 registros** distribuídos em **7 categorias** (`Escala e Acesso`, `Financiamento e Infraestrutura`, `Desempenho Internacional (PISA)`, `Evolução Histórica`, `Equidade e Índices Globais`, `Desigualdades Regionais (Censo 2020)` e `Desigualdades Estruturais`), contendo as colunas:
* `Categoria`, `Indicador`, `Valor`, `Unidade`, `Ano_Referencia`, `Recorte_Regional` e `Observacoes`.

### 3.3. Modelagem SQL & Pipeline Python (`schema_e_consultas.sql` e `analise_indicadores.py`)
* **`schema_e_consultas.sql`:** Define o schema relacional (`CREATE TABLE indicadores_educacao_china`) compatível com SQLite, PostgreSQL e MySQL, além de consultas analíticas para agregação por categoria, evolução censitária, ranking PISA 2025 e disparidades Leste–Oeste.
* **`analise_indicadores.py`:** Lê a base de dados, higieniza valores textuais e numéricos (tratando decimais, milhares e operadores como `>`), persiste os dados em um banco local `educacao_china.db` via `sqlite3` e executa as consultas analíticas com `pandas`.

---

## 4. Principais Resultados das Análises

| Eixo Analítico | Indicador / Recorte | Resultado |
| :--- | :--- | :--- |
| **Escala & Acesso (2025)** | Total de estudantes na educação formal | 280,40 milhões |
| **Escala & Acesso (2025)** | Conclusão da educação compulsória (9 anos) | 96,1% |
| **Escala & Acesso (2025)** | Taxa bruta de matrícula no ensino superior | 61,3% (48,73 milhões de estudantes) |
| **Desempenho PISA 2025** | Matemática — Grupo B-S-J-Z (vs. média OCDE) | 612 pontos (+149 pts acima da OCDE) |
| **Evolução Histórica** | Taxa de analfabetismo (1982 → 2020) | Queda de 22,81% para 2,67% |
| **Evolução Histórica** | Escolaridade média nacional (1990 → 2020) | Aumento de 5,52 para 9,91 anos |
| **Assimetria Regional (2020)** | Escolaridade média: Pequim vs. Tibete | 12,64 anos (Pequim) vs. 6,75 anos (Tibete) |

---

## 5. Como Executar Localmente

### 5.1. Clonar o Repositório
```bash
git clone [https://github.com/verissimomv/](https://github.com/verissimomv/)<nome-do-repositorio>.git
cd <nome-do-repositorio>
```

### 5.2. Visualizar a Aplicação Web (`index.html`)
Abra o arquivo `index.html` diretamente em qualquer navegador moderno ou inicie um servidor local simples com Python:

```bash
python -m http.server 8000
```
Em seguida, acesse `http://localhost:8000` no navegador.

### 5.3. Executar o Pipeline SQL + Python (`analise_indicadores.py`)
Certifique-se de ter o Python 3.8+ e a biblioteca `pandas` instalados:

```bash
pip install pandas
python analise_indicadores.py
```

---

## 6. Publicação via GitHub Pages

1. Acesse o repositório no GitHub e clique na aba **Settings**.
2. No menu lateral esquerdo, selecione **Pages** (na seção *Code and automation*).
3. Em **Build and deployment > Branch**, escolha `main` e a pasta `/ (root)`, depois clique em **Save**.
4. Aguarde cerca de 1 a 2 minutos e acesse o site publicado em:
   `https://verissimomv.github.io/<nome-do-repositorio>/`

---

## 7. Referências e Fontes dos Dados

* **Ministério da Educação da República Popular da China (MOE):** Boletins estatísticos nacionais de desenvolvimento educacional (2023–2026).
* **OCDE (PISA 2012 & 2025):** Relatórios de avaliação internacional de estudantes (amostra B-S-J-Z: Pequim, Xangai, Jiangsu e Zhejiang).
* **National Bureau of Statistics of China (NBS):** Séries históricas dos Censos Demográficos Nacionais (1982–2020).
* **Literatura Acadêmica:** Estudos sobre financiamento educacional, reforma do sistema *Hukou*, política de *Dupla Redução* (*Shuangjian*) e decomposição do Índice de Desenvolvimento Humano (IDH) chinês.

---

## Autor

Desenvolvido por **[verissimomv](https://github.com/verissimomv)**.
