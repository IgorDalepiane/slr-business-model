# Prompt: Extração de Dados de Questões Fechadas (Closed-Ended Questions)

## Objetivo

Processar todos os artigos na pasta `raw_data/` e extrair dados de uma questão específica, consolidando-os em um arquivo CSV dentro da pasta `by_closed_ended_question/`.

## Instruções Gerais

### 1. Arquivo de Saída

- **Nome do arquivo**: `question_XX.csv` (onde XX é o número da questão)
- **Localização**: `by_closed_ended_question/`
- **IMPORTANTE**: Criar APENAS este arquivo, não criar nenhum outro arquivo adicional

### 2. Fonte de Dados

- **Pasta de origem**: `raw_data/`
- **Processar**: TODOS os arquivos `.json` presentes na pasta
- **Atenção**: Os valores presentes nos JSONs são de extrema importância e NÃO devem ser modificados

### 3. Formato do CSV

O arquivo CSV deve conter as seguintes colunas (header):

```
article_id,article_title,response_found,values_inside_scope,extracted_value,confidence_level,source_citation
```

#### Descrição dos Campos:

- **article_id**: ID do artigo (extraído do JSON)
- **article_title**: Título do artigo (extraído do JSON)
- **response_found**: Indica se a resposta foi encontrada (extraído do JSON)
- **values_inside_scope**: Valores que estão dentro do escopo definido para a questão (ver seção específica abaixo)
- **extracted_value**: Valor extraído completo (extraído do JSON)
- **confidence_level**: Nível de confiança da extração (extraído do JSON)
- **source_citation**: Citação da fonte no artigo (extraído do JSON)

### 4. Campo Especial: `values_inside_scope`

Este campo requer processamento adicional:

1. **Analisar** o conteúdo de `extracted_value`
2. **Comparar** com a lista de valores válidos para o escopo da questão (ver seção "Escopo da Questão")
3. **Extrair** os valores que estão presentes em `extracted_value`:
   - Priorizar valores que correspondem exatamente à lista de valores válidos
   - Se houver valores relacionados mas não exatamente na lista (ex: "Open Source" genérico), incluí-los também
   - Usar o termo como aparece em `extracted_value` quando relevante para a análise
4. **NÃO inventar** valores que não estejam explicitamente em `extracted_value`
5. **Separador**: Quando múltiplos valores forem identificados, separá-los com ";" (ponto e vírgula)
   - Exemplo: `B2B;B2C;Enterprise`
6. **Propósito**: Este campo será usado para gerar gráficos futuramente, portanto a precisão é crítica

### 5. Fluxo de Trabalho

1. **Criar TODOs** para organizar o trabalho e ser mais eficiente
2. **Listar** todos os arquivos JSON em `raw_data/`
3. **Iterar** por cada arquivo JSON:
   - Ler o arquivo
   - Localizar os dados da questão específica
   - Extrair os campos necessários
   - Processar o campo `values_inside_scope`
   - Adicionar linha ao CSV
4. **Conferir TUDO duas vezes**:
   - Verificar se todos os JSONs foram processados
   - Verificar se os valores extraídos correspondem exatamente aos valores nos JSONs
   - Verificar se `values_inside_scope` contém valores que estão em `extracted_value`
   - Verificar formatação do CSV
5. **Atualizar arquivo de estatísticas** `by_closed_ended_question/STATISTICS.md`:
   - Adicionar/atualizar seção da questão processada
   - Incluir estatísticas: total, com resposta, sem resposta, com valores
   - Criar tabela de distribuição de valores com quantidades e percentuais
   - **Documentar decisões importantes**: casos especiais, correções manuais, valores excluídos
   - Anotar quando `extracted_value` menciona algo mas não foi incluído em `values_inside_scope` (e porquê)

### 6. Regras de Qualidade

- ✅ **FAZER**: Extrair valores exatamente como aparecem nos JSONs
- ✅ **FAZER**: Conferir duas vezes todos os dados
- ✅ **FAZER**: Garantir que `values_inside_scope` ⊆ `extracted_value` (sempre vem de `extracted_value`)
- ✅ **FAZER**: Incluir valores relacionados mesmo que não estejam exatamente na lista (ex: "Open Source" genérico)
- ✅ **FAZER**: Documentar no STATISTICS.md decisões sobre valores excluídos/incluídos e porquê
- ✅ **FAZER**: Anotar casos onde `extracted_value` tem conteúdo mas `values_inside_scope` ficou vazio (explicar razão)
- ❌ **NÃO FAZER**: Modificar valores dos JSONs
- ❌ **NÃO FAZER**: Inventar ou inferir valores que não estão explícitos em `extracted_value`
- ❌ **NÃO FAZER**: Criar arquivos adicionais além do CSV e atualização do STATISTICS.md

---

## Escopo Específico por Questão

### Questão 04: Target Customer Type

**Descrição completa:** What is the target customer type of the software business model presented in the article?
- Classify the main target audience of the software business model according to the size and nature of the customer this model intends to serve
- Identify the customer type most emphasized in the article as the primary target of the software business model

**Tipo:** Single selection

**Valores válidos para `values_inside_scope`:**
```
[B2C, B2B SMB, B2B, Mid-market, Enterprise, Developers/Dev-tools, Government, Others]
```

**Notas específicas:**
- Os valores devem corresponder exatamente aos listados acima
- Esta é uma questão de seleção única, mas se `extracted_value` mencionar múltiplos tipos, incluir todos em `values_inside_scope` separados por ";"
- Caso `extracted_value` não contenha nenhum valor da lista, `values_inside_scope` deve ficar vazio

---

### Questão 08: Type of Product or Service

**Descrição completa:** What is the type of product or service offered by the software business model presented in the article?
- Classify the fundamental nature of the software offering in the business model presented in the article
- There may be multiple categories if the software business model encompasses different types of software products or services

**Tipo:** Multiple selection

**Valores válidos para `values_inside_scope`:**
```
[Application, Platform, API, SDK, Data, Managed Service, Infrastructure, Others]
```

**Notas específicas:**
- Esta é uma questão de múltipla seleção - podem existir múltiplos valores
- Separar múltiplos valores com ";"
- Apenas incluir valores que estejam explicitamente mencionados em `extracted_value`

---

### Questão 09: Software Delivery or Deployment

**Descrição completa:** How is the software delivered or deployed in the business model presented in the article?
- Identify the technical modalities for software availability described in the business model presented in the article
- All forms of software delivery or deployment mentioned in the article, with percentages if available

**Tipo:** Multiple selection

**Valores válidos para `values_inside_scope`:**
```
[On-premises, Single-tenant cloud, Multi-tenant SaaS, Edge, Mobile, Desktop, Others]
```

**Notas específicas:**
- Esta é uma questão de múltipla seleção
- Separar múltiplos valores com ";"
- Se `extracted_value` contiver percentagens, ignorá-las em `values_inside_scope` (apenas os tipos)
- Exemplo: se `extracted_value` = "Multi-tenant SaaS (70%), On-premises (30%)", então `values_inside_scope` = "Multi-tenant SaaS;On-premises"

---

### Questão 10: Intellectual Property Regime

**Descrição completa:** What is the intellectual property regime adopted by the software business model presented in the article?
- Identify how the software is licensed and distributed as described in the business model presented in the article
- The main software licensing regime mentioned in the article, with observations about variations if any

**Tipo:** Single selection

**Valores válidos para `values_inside_scope`:**
```
[Proprietary, Permissive Open Source, Copyleft, Dual License, Open Core, Others]
```

**Notas específicas:**
- Esta é uma questão de seleção única
- Se `extracted_value` mencionar múltiplos regimes, incluir todos em `values_inside_scope` separados por ";"
- Aceitar valores relacionados como "Open Source" genérico se aparecer em `extracted_value` (mesmo não estando na lista específica)
- Ignorar observações textuais adicionais, focar nos valores de licenciamento

---

### Questão 12: Revenue Sources

**Descrição completa:** What are the revenue sources of the software business model presented in the article?
- Identify all ways the software business model generates revenue as described in the article
- All revenue sources mentioned in the article about the software business model, prioritizing by importance if indicated

**Tipo:** Multiple selection

**Valores válidos para `values_inside_scope`:**
```
[Perpetual license, Subscription, Usage/consumption, Transaction, Advertising, Support, Dual licensing, Open core, Marketplace fees, Others]
```

**Notas específicas:**
- Esta é uma questão de múltipla seleção
- Separar múltiplos valores com ";"
- Ignorar indicações de prioridade/importância, incluir apenas os valores da lista

---

### Questão 13: Pricing Base Unit

**Descrição completa:** What is the base unit for pricing of the software business model presented in the article?
- Identify on which metric the software price is calculated as described in the business model presented in the article
- The main billing unit most emphasized in the article about the software business model

**Tipo:** Single selection

**Valores válidos para `values_inside_scope`:**
```
[User/seat, MAU, API calls, Computing time, Storage, Transactions, Devices, Revenue sharing, Others]
```

**Notas específicas:**
- Esta é uma questão de seleção única
- Se `extracted_value` mencionar múltiplas unidades, incluir todas em `values_inside_scope` separadas por ";"

---

### Questão 14: Price Presentation Structure

**Descrição completa:** What is the price presentation structure of the software business model described in the article?
- How software prices are organized and presented to customers as described in the business model presented in the article
- All price structures used simultaneously in the software business model as mentioned in the article

**Tipo:** Multiple selection

**Valores válidos para `values_inside_scope`:**
```
[Freemium, Trial, Tiers/Plans, Pay-as-you-go, Prepaid credits, Annual contract, Custom negotiation, Others]
```

**Notas específicas:**
- Esta é uma questão de múltipla seleção
- Separar múltiplos valores com ";"
- Podem coexistir múltiplas estruturas simultaneamente

---

### Questão 16: Company Role in Ecosystem

**Descrição completa:** What is the role of the offering company in the ecosystem of the software business model presented in the article?
- Classify how the company implementing the software business model positions itself in relation to other actors as described in the article
- The predominant role or most emphasized in the article about how the offering company positions itself in the software business model ecosystem

**Tipo:** Single selection

**Valores válidos para `values_inside_scope`:**
```
[Standalone product, Two-sided platform, Marketplace, OEM component, Plugin/Complement, Others]
```

**Notas específicas:**
- Esta é uma questão de seleção única
- Se `extracted_value` mencionar múltiplos papéis, incluir todos em `values_inside_scope` separados por ";"

---

### Questão 17: Network Effect Type

**Descrição completa:** What type of network effect is present in the software business model presented in the article?
- Identify if and how the software value increases with more users as described in the business model presented in the article
- The most significant or clearly described network effect in the article about the software business model

**Tipo:** Single selection

**Valores válidos para `values_inside_scope`:**
```
[None, Direct (more users = more value), Cross-sided (distinct groups benefit), Data (more data = better product), Others]
```

**Notas específicas:**
- Esta é uma questão de seleção única
- Incluir o valor completo conforme listado (incluindo a descrição entre parênteses se presente)
- Se `extracted_value` mencionar múltiplos tipos de network effect, incluir todos em `values_inside_scope` separados por ";"

---

### Questão 18: Customer Acquisition Channels

**Descrição completa:** What are the customer acquisition channels of the software business model presented in the article?
- Identify how new customers discover and adopt the software as described in the business model presented in the article
- All customer acquisition channels mentioned in the article as relevant to the software business model

**Tipo:** Multiple selection

**Valores válidos para `values_inside_scope`:**
```
[Product-led Growth, Direct sales, Partners/channels, Marketplaces, Digital marketing, Referral, Others]
```

**Notas específicas:**
- Esta é uma questão de múltipla seleção
- Separar múltiplos valores com ";"
- Podem coexistir múltiplos canais simultaneamente

---

### Questão 19: Cloud Marketplaces Usage

**Descrição completa:** Does the software business model presented in the article use cloud marketplaces or platforms?
- Verify if there is presence in specific distribution platforms as mentioned in the software business model presented in the article
- Marketplace or cloud platforms explicitly mentioned in the article about the software business model
- **Escopo expandido:** Inclui enterprise cloud marketplaces, mobile app stores, gaming platforms e outros marketplaces de distribuição de software

**Tipo:** Yes/No + List (múltipla seleção)

**Valores válidos para `values_inside_scope`:**
```
[AWS Marketplace, Azure Marketplace, Google Cloud Marketplace, Atlassian Marketplace, Salesforce AppExchange, Apple App Store, Google Play Store, Steam, Others]
```

**Notas específicas:**
- Esta é uma questão especial: Yes/No + Lista
- Em `values_inside_scope`, incluir APENAS os nomes dos marketplaces/platforms da lista (ignorar o Yes/No)
- Se a resposta for "No" ou nenhum marketplace específico for mencionado, `values_inside_scope` deve ficar vazio
- Separar múltiplos marketplaces com ";"

**Categorias de marketplaces/platforms:**
1. **Enterprise Cloud Marketplaces:** AWS Marketplace, Azure Marketplace, Google Cloud Marketplace, Atlassian Marketplace, Salesforce AppExchange
2. **Mobile App Stores:** Apple App Store, Google Play Store
3. **Gaming Platforms:** Steam
4. **Others:** Qualquer outro marketplace/platform de distribuição de software não listado acima
   - Exemplos: Origin, SourceForge, Chinese app stores, regional cloud marketplaces, proprietary marketplaces, carrier stores, etc.

**Critérios de inclusão:**
- Marketplace/platform deve ser usado para **distribuição/venda** de software
- Mencionar apenas uso de IaaS/PaaS (ex: hospedar em AWS) NÃO conta como marketplace
- App stores de operadoras (carrier stores) contam como "Others"
- Marketplaces proprietários/internos contam como "Others"

---

### Questão 30: Type of Evidence

**Descrição completa:** What is the type of evidence presented in the article about the software business model?
- Classify the methodological nature of the software business model study as presented in the article
- Type of investigation or main data source used in the article to study the software business model

**Tipo:** Single selection

**Valores válidos para `values_inside_scope`:**
```
[Single case study, Multiple cases, Survey, Experiment, Secondary data analysis, Literature review, Expert opinion, Others]
```

**Notas específicas:**
- Esta é uma questão de seleção única
- Se `extracted_value` mencionar múltiplos tipos de evidência, incluir todos em `values_inside_scope` separados por ";"

---

## Template de TODOs Sugeridos

```
[ ] 1. Criar arquivo question_XX.csv com header correto
[ ] 2. Listar todos os arquivos JSON em raw_data/
[ ] 3. Para cada JSON (XX/YY processados):
    [ ] 3.1. Ler arquivo JSON
    [ ] 3.2. Extrair dados da questão XX
    [ ] 3.3. Processar values_inside_scope
    [ ] 3.4. Adicionar linha ao CSV
[ ] 4. Verificação (1ª passada):
    [ ] 4.1. Todos os JSONs foram processados?
    [ ] 4.2. Valores correspondem aos JSONs?
    [ ] 4.3. values_inside_scope está correto?
[ ] 5. Verificação (2ª passada):
    [ ] 5.1. Revisar formato do CSV
    [ ] 5.2. Revisar campos obrigatórios
    [ ] 5.3. Revisar separadores em values_inside_scope
[ ] 6. Atualizar STATISTICS.md:
    [ ] 6.1. Adicionar/atualizar seção da questão
    [ ] 6.2. Incluir estatísticas e distribuição
    [ ] 6.3. Documentar decisões e casos especiais
```

---

## Exemplo de Saída (Questão 04)

```csv
article_id,article_title,response_found,values_inside_scope,extracted_value,confidence_level,source_citation
190638760,"Impact of AI on Business",yes,B2B;Enterprise,"The study focuses on B2B and Enterprise markets",high,"Section 3.2, page 45"
190638781,"Consumer Behavior Analysis",yes,B2C,"B2C market analysis",medium,"Introduction, page 3"
190638871,"Government Digital Transformation",yes,Government,"Government sector implementation",high,"Chapter 4"
```

---

## Notas Finais

- Este prompt pode ser adaptado para diferentes questões fechadas
- Sempre atualizar a seção "Escopo Específico por Questão" com os valores válidos apropriados
- A precisão dos dados em `values_inside_scope` é crítica para análises posteriores
- Manter a consistência no formato do CSV em todas as questões

## Arquivo STATISTICS.md

### Propósito
O arquivo `by_closed_ended_question/STATISTICS.md` é um repositório consolidado de dados analíticos de todas as questões processadas. Serve como base para:
- Geração de gráficos e visualizações
- Análises comparativas entre questões
- Documentação de decisões metodológicas
- Rastreamento de padrões e insights

### Estrutura de cada seção
Para cada questão processada, incluir:

1. **Cabeçalho**: Número e texto completo da questão
2. **Tipo**: Single/Multiple selection
3. **Estatísticas gerais**:
   - Total de artigos
   - Artigos com resposta (N e %)
   - Artigos sem resposta (N e %)
   - Artigos com valores identificados (N e %)
4. **Tabela de distribuição**: Cada valor com quantidade e percentual
5. **Observações/Notas**: 
   - Padrões identificados
   - Casos especiais
   - Decisões de inclusão/exclusão
   - Correções manuais aplicadas
   - Valores em `extracted_value` excluídos de `values_inside_scope` (com justificativa)

### Exemplo de documentação de decisões
```markdown
**Decisões Documentadas:**

#### Casos especiais corrigidos:
- **190654720**: "bounded number of monthly predictions" → Others
  - Razão: Unidade específica não prevista na lista

#### Casos mantidos vazios (correto):
- **190655589**: Apenas "usage/consumption" genérico
  - Razão: É modelo de receita, não unidade de precificação
  - A questão pede a unidade base (o que é medido), não como é cobrado
```

### Atualização
- O arquivo deve ser atualizado **após cada processamento** de questão
- Manter ordem numérica das questões
- Atualizar seção "Insights Gerais" quando adicionar nova questão
- Registrar data da última atualização no topo do arquivo

