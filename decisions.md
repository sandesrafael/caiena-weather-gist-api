# Decisões Técnicas

Este documento explica as principais decisões arquiteturais e técnicas adotadas durante o desenvolvimento.


## 1. Por que Clean Architecture Simplificada?

O objetivo foi:

- Garantir separação clara de responsabilidades
- Maximizar testabilidade
- Evitar complexidade desnecessária
- Manter o projeto legível e organizado

Dado o escopo do desafio, foi escolhida uma versão leve da Clean Architecture, evitando overengineering.

## 2. Por que criar um SDK para o OpenWeather?

O desafio exige a criação de uma biblioteca que funcione como SDK.

Além disso, isso proporciona:

- Encapsulamento da lógica HTTP
- Facilidade para mock em testes
- Redução de acoplamento com a camada de aplicação


## 3. Por que usar exceções customizadas?

Exceções customizadas evitam:

- Vazamento de erros de bibliotecas externas
- Mistura de erros técnicos com regra de negócio

Elas permitem:

- Propagação controlada de erros
- Mapeamento adequado para respostas HTTP
- Código mais claro e previsível


## 4. Por que calcular a média diária internamente?

O endpoint gratuito de previsão do OpenWeather retorna dados em intervalos de 3 horas.

Para atender ao requisito do desafio (média diária dos próximos 5 dias), a aplicação:

- Agrupa os dados por data
- Calcula a média diária
- Limita o resultado aos próximos 5 dias

Essa lógica foi posicionada na camada de Domínio para garantir isolamento e testabilidade.


## 5. Por que aplicar Inversão de Dependência?

A camada de aplicação depende de abstrações, não de implementações concretas.

Benefícios:

- Alta testabilidade (uso fácil de mocks)
- Baixo acoplamento
- Facilidade de evolução
- Separação clara entre regra de negócio e infraestrutura


## 6. Por que utilizar Docker?

Docker garante:

- Ambiente reprodutível
- Facilidade de demonstração
- Ausência de conflitos de dependência
- Padronização do ambiente de execução

## 7. Decisões adicionais da API
- SDK instalado como dependência Git (mantém dois repositórios como exigido no desafio original)
- Gist fixo via variável de ambiente (mais simples e seguro)
- Comentário formatado exatamente como no exemplo do PDF
- Tratamento de erros mapeado para HTTP 400/500