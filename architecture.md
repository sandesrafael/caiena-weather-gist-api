# Visão Geral da Arquitetura

## 1. Objetivo

Esta aplicação integra com:

- API OpenWeatherMap
- API de Gist do GitHub

Ela expõe um endpoint HTTP que:

1. Recebe o nome de uma cidade
2. Obtém o clima atual e a previsão para 5 dias
3. Calcula a média diária das temperaturas
4. Monta uma mensagem formatada
5. Publica a mensagem como comentário em um Gist do GitHub


## 2. Estilo Arquitetural

O projeto segue uma abordagem de Clean Architecture simplificada, com clara separação de responsabilidades:

Camada HTTP (FastAPI) -> Camada de Aplicação (Casos de Uso) -> 
Camada de Domínio (Regras de Negócio) -> Camada de Infraestrutura (Integrações Externas)


## 3. Responsabilidades das Camadas

### Camada de API (app/api)
- Recebe requisições HTTP
- Valida parâmetros de entrada
- Chama os serviços da aplicação
- Converte exceções em respostas HTTP
- Não contém regra de negócio


### Camada de Aplicação (app/application)
- Orquestra o caso de uso
- Coordena domínio e infraestrutura
- Depende apenas de abstrações (interfaces)
- Aplica inversão de dependência

Principal ponto de entrada:
WeatherCommentService


### Camada de Domínio (app/domain)
- Contém as regras de negócio
- Não depende de bibliotecas externas
- Inclui:
  - Cálculo de média diária
  - Modelos de domínio

Essa camada é totalmente testável de forma isolada.


### Camada de Infraestrutura (app/infrastructure)
- Implementa integrações externas:
  - Cliente OpenWeather
  - Cliente GitHub Gist
- Converte JSON externo em modelos de domínio
- Lança exceções padronizadas da aplicação


### Camada Core (app/core)
- Configurações da aplicação
- Definição de exceções customizadas


## 4. Fluxo de Dependências

Infraestrutura → Aplicação → Domínio
API → Aplicação

A camada de Domínio não depende de nenhuma outra camada.

Isso garante:
- Alta testabilidade
- Baixo acoplamento
- Facilidade de evolução


## 5. Extensibilidade

A aplicação utiliza contratos (interfaces) para:

- WeatherProvider
- GistPublisher

Isso permite substituir implementações sem alterar a lógica de negócio.

Exemplo:
- Migrar de `requests` para `httpx`
- Trocar OpenWeather por outro provedor


## 6. Estratégia de Tratamento de Erros

Foram criadas exceções customizadas para:

- Evitar vazamento de erros da infraestrutura
- Manter separação clara de responsabilidades
- Permitir mapeamento adequado para códigos HTTP


## 7. Filosofia de Testes

- A lógica de domínio é testada isoladamente
- A camada de aplicação é testada com mocks
- A camada de API é testada com TestClient do FastAPI
- APIs externas nunca são chamadas durante testes unitários