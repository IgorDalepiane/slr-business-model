# Visualização por Questões Abertas

Este diretório contém dados extraídos dos artigos organizados por questão aberta.

## Estrutura

Cada arquivo `question_XX.json` contém todas as respostas de todos os artigos para uma questão específica.

## Questões Abertas Incluídas

| Arquivo          | ID  | Questão                                         | Artigos com Resposta |
| ---------------- | --- | ----------------------------------------------- | -------------------- |
| question_01.json | 1   | Nome e definição do modelo de negócio           | 67/67                |
| question_02.json | 2   | Sinônimos ou termos alternativos                | 67/67                |
| question_03.json | 3   | Segmento vertical ou indústria principal        | 67/67                |
| question_05.json | 5   | Tamanho típico das empresas ofertantes          | 64/67                |
| question_06.json | 6   | Região geográfica                               | 65/67                |
| question_07.json | 7   | Segmento específico de cliente                  | 66/67                |
| question_11.json | 11  | Restrições ou compatibilidades de licenciamento | 25/67                |
| question_15.json | 15  | Moeda e periodicidade de cobrança               | 26/67                |
| question_20.json | 20  | Elementos do Business Model Canvas              | 63/67                |
| question_21.json | 21  | Atores do ecossistema e interações              | 67/67                |
| question_22.json | 22  | Motivações para adoção                          | 67/67                |
| question_23.json | 23  | Fatores de sucesso                              | 67/67                |
| question_24.json | 24  | Pré-requisitos ou condições necessárias         | 67/67                |
| question_25.json | 25  | Restrições ou incompatibilidades                | 67/67                |
| question_26.json | 26  | Desafios na implementação                       | 67/67                |
| question_27.json | 27  | Práticas de mitigação de desafios               | 67/67                |
| question_28.json | 28  | Métricas e resultados quantitativos             | 64/67                |
| question_29.json | 29  | Período temporal e maturidade                   | 67/67                |
| question_31.json | 31  | Empresas ou produtos citados como exemplos      | 64/67                |
| question_32.json | 32  | Variações ou subtipos do modelo                 | 67/67                |
| question_33.json | 33  | Tendências futuras ou evoluções                 | 67/67                |

## Formato dos Arquivos

Cada arquivo JSON contém:

```json
{
  "question_metadata": {
    "question_id": "1",
    "question_text": "Texto completo da questão",
    "total_articles": 67,
    "articles_with_response": 67,
    "articles_without_response": 0
  },
  "responses_by_article": [
    {
      "article_id": "190638760",
      "article_title": "Título do artigo",
      "extraction_date": "2025-10-07",
      "question_id": "1",
      "question_text": "Texto da questão",
      "response_found": true,
      "extracted_value": "Resposta extraída",
      "synonyms_found": ["termo1", "termo2"],
      "source_citation": "Citação da fonte",
      "confidence_level": "high"
    }
  ]
}
```

## Estatísticas

- **Total de artigos processados**: 67
- **Total de questões abertas**: 21
- **Questões com 100% de respostas**: 17
- **Questões com menor taxa de resposta**:
  - Questão 11 (Restrições de licenciamento): 37%
  - Questão 15 (Moeda e periodicidade): 39%

## Uso

Para análise comparativa de como diferentes artigos responderam à mesma questão aberta, basta abrir o arquivo correspondente à questão de interesse.

## Data de Geração

Este diretório foi gerado automaticamente a partir dos dados em `raw_data/`.
