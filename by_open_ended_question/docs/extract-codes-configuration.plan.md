<!-- 73c850ce-76dd-4e4f-bd9d-a16e6e9c3325 feeca19d-4caa-4ece-bd0f-e481981c03aa -->
# Extração de Códigos Qualitativos dos Artigos

## Contexto

Processar 21 arquivos JSON contendo respostas de 67 artigos sobre modelos de negócio de software, extraindo códigos qualitativos (temas/conceitos) a partir das citações (`source_citation`) de cada artigo.

## Arquivos a Processar

- question_01.json (nome e definição do modelo)
- question_02.json (sinônimos e termos alternativos)
- question_03.json (segmento vertical/indústria)
- question_05.json (tamanho das empresas)
- question_06.json (região geográfica)
- question_07.json (segmento de clientes)
- question_11.json (restrições de licenciamento)
- question_15.json, question_20.json, question_21.json, question_22.json, question_23.json, question_24.json, question_25.json, question_26.json, question_27.json, question_28.json, question_29.json, question_31.json, question_32.json, question_33.json

## Estratégia de Extração

### 1. Análise Incremental por Arquivo

Para cada arquivo JSON:

- Ler campo `source_citation` de cada artigo
- Identificar frases/sentenças significativas (quotes)
- Extrair conceitos e temas principais

### 2. Estrutura Hierárquica de Códigos

Criar códigos em dois níveis:

- **CLASS** (categoria principal): temas abrangentes
- **SUBCLASS** (subcategoria): temas específicos dentro da classe

Exemplos esperados baseados nos dados visualizados:

- Class: "Business model characteristics"
  - Subclass: "Delivery model" → Code: "Cloud delivery model"
  - Subclass: "Pricing strategy" → Code: "Subscription-based pricing"
- Class: "Technical architecture"
  - Subclass: "Infrastructure" → Code: "Multi-tenant architecture"
- Class: "Market positioning"
  - Subclass: "Customer segments" → Code: "SME market focus"

### 3. Consolidação e Deduplicação

- Mesclar códigos similares usando nomes consistentes
- Evitar redundâncias
- Manter organização clara

## Formato de Saída

```json
{
  "codes_config": [
    {
      "code": "Cloud delivery model",
      "description": "Software distribution through cloud infrastructure",
      "class": "Business model characteristics",
      "subclass": "Delivery model"
    },
    {
      "code": "Subscription-based pricing",
      "description": "Recurring payment model for software access",
      "class": "Business model characteristics",
      "subclass": "Pricing strategy"
    }
  ]
}
```

## Principais Temas Identificados (preliminar)

Baseado na análise inicial dos 3 primeiros arquivos:

**Business Model Types:**

- SaaS, Freemium, Open Source, Platform, Subscription, Games-as-a-Service

**Delivery & Architecture:**

- Cloud computing, Multi-tenant, Remote hosting, On-demand access

**Pricing & Revenue:**

- Pay-as-you-go, Subscription fees, Perpetual licensing, Usage-based

**Market Segments:**

- Enterprise, SME, B2B, B2C, Cross-industry

**Geographic Distribution:**

- USA-dominant, Global, Regional (Europe, Asia)

**Company Characteristics:**

- Startups, Established vendors, Spin-offs, Young companies

## Arquivo de Destino

`by_open_ended_question/analysis/codes_config.json`

## Observações

- Seguir rigorosamente o formato JSON especificado no prompt
- Usar `null` para subclass quando não aplicável
- Manter labels concisos em inglês
- Focar em códigos derivados das citações reais (source_citation)
- Não incluir comentários ou explicações no JSON final