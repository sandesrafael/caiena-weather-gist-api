# Weather Gist API - Desafio Caiena

API que recebe uma cidade e publica automaticamente um comentário em um Gist com temperatura atual + média dos próximos 5 dias.

## Pré-requisitos
1. Chave OpenWeatherMap (gratuita)
2. Token clássico do GitHub com escopo **gist**
3. Um Gist criado (pode ser vazio) → copie o ID da URL (ex: `1a2b3c4d5e6f...`)

## Configuração
```bash
# 1. Instale o SDK primeiro (do outro repo)
cd ../caiena-openweather-sdk
pip install -e .

# 2. Volte para a API
cd ../caiena-weather-gist-api
pip install -r requirements.txt

# 3. Configure .env
cp .env.example .env