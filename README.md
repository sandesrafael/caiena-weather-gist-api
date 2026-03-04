# Weather Gist API - Desafio Caiena

## Pre-requisitos

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) instalado
- Chave de API do [OpenWeatherMap](https://openweathermap.org/api)
- Token classico do GitHub com escopo `gist`
- Um Gist criado (pode ser vazio) — copie o ID da URL

## Configuracao

```bash
# 1. Crie o ambiente virtual
uv venv

# 2. Instale dependencias
uv pip install -r requirements.txt

# 3. Configure variaveis de ambiente
cp .env.example .env
```

Edite o `.env` com suas chaves:

```env
OPENWEATHER_API_KEY=sua_chave_aqui
GITHUB_TOKEN=seu_token_classico_aqui
GIST_ID=id_do_gist_aqui
```

> O SDK e instalado automaticamente via `requirements.txt` (`git+https`).
> Nao e necessario clonar o repositorio do SDK.

## Execucao local

```bash
uv run uvicorn app.main:app --reload
```

- API: `http://localhost:8000`
- Docs interativa: `http://localhost:8000/docs`

## Execucao com Docker Compose

```bash
docker-compose up --build
```

## Testes

```bash
uv run pytest
```
