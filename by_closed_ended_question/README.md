# Questões Fechadas - Resultados Consolidados

Este diretório contém os resultados consolidados da extração de dados para questões fechadas (closed-ended questions).

## Estrutura de Arquivos

### Arquivos de Dados

- `question_04.csv` - Target Customer Type
- `question_08.csv` - Type of Product or Service
- `question_09.csv` - Software Delivery or Deployment
- `question_10.csv` - Intellectual Property Regime
- `question_12.csv` - Revenue Sources
- `question_13.csv` - Pricing Base Unit

Cada CSV contém:
- `article_id` - ID do artigo
- `article_title` - Título do artigo
- `response_found` - Se a resposta foi encontrada (yes/no)
- `values_inside_scope` - Valores identificados dentro do escopo da questão
- `extracted_value` - Valor extraído completo do JSON
- `confidence_level` - Nível de confiança (high/medium/low)
- `source_citation` - Citação da fonte no artigo

### Arquivos Analíticos

#### `STATISTICS.md`
Arquivo consolidado com estatísticas e insights de todas as questões processadas.

**Contém:**
- Estatísticas gerais por questão (total, com resposta, distribuição de valores)
- Tabelas de distribuição com percentuais
- Insights e padrões identificados
- Decisões metodológicas documentadas
- Casos especiais e correções aplicadas

**Uso:** Base para geração de gráficos, visualizações e análises comparativas.

#### `generate_stats.py`
Script utilitário para gerar estatísticas de questões.

**Uso:**
```bash
# Ver estatísticas de uma questão
python3 generate_stats.py 13

# Usar em scripts Python
from generate_stats import analyze_question
stats = analyze_question('13')
```

## Formato dos Dados

### Campo `values_inside_scope`
Contém valores identificados que correspondem à lista de valores válidos da questão:
- Valores separados por `;` (ponto e vírgula)
- Exemplo: `B2B;B2C;Enterprise`
- Vazio quando `extracted_value` não contém valores da lista válida

**Importante:** Este campo é usado para geração de gráficos e análises quantitativas.

### Valores Válidos por Questão

Ver arquivo `../prompts/prompt_closed_ended_extraction.md` para lista completa de valores válidos de cada questão.

## Processo de Extração

1. **Fonte:** Arquivos JSON em `../raw_data/`
2. **Prompt:** `../prompts/prompt_closed_ended_extraction.md`
3. **Processamento:** Para cada questão:
   - Extrair dados dos JSONs
   - Identificar valores dentro do escopo
   - Gerar CSV consolidado
   - Atualizar STATISTICS.md

## Qualidade dos Dados

### Verificações Aplicadas
- ✅ Todos os 67 artigos processados
- ✅ Valores correspondem exatamente aos JSONs originais
- ✅ `values_inside_scope` ⊆ `extracted_value`
- ✅ Formato CSV consistente

### Casos Documentados
Decisões sobre inclusão/exclusão de valores são documentadas em `STATISTICS.md` na seção de cada questão.

## Uso dos Dados

### Para Análises
```python
import csv
import pandas as pd

# Carregar dados
df = pd.read_csv('question_13.csv')

# Análises
print(f"Taxa de resposta: {df['response_found'].value_counts()}")
print(f"Valores mais comuns: {df['values_inside_scope'].value_counts()}")
```

### Para Gráficos
Os dados em `values_inside_scope` estão prontos para visualização:
- Gráficos de barras (distribuição de valores)
- Gráficos de pizza (proporções)
- Heatmaps (cruzamento entre questões)
- Análises temporais

## Manutenção

### Adicionar Nova Questão
1. Processar dados seguindo `../prompts/prompt_closed_ended_extraction.md`
2. Criar arquivo `question_XX.csv`
3. Atualizar `STATISTICS.md` com nova seção
4. Testar com `generate_stats.py XX`

### Atualizar Dados Existentes
Se correções forem necessárias:
1. Aplicar correções no CSV
2. Atualizar seção correspondente em `STATISTICS.md`
3. Documentar mudanças em "Decisões Documentadas"

## Histórico

- **2025-10-11**: Criação do diretório e processamento inicial
  - Questões processadas: 04, 08, 09, 10, 12, 13
  - Total: 67 artigos
  - Arquivo STATISTICS.md criado com dados consolidados

