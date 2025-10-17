# Automação Agro Teste

## Descrição

Este projeto automatiza o processo de preenchimento e envio de romaneios utilizando o Playwright para automação de navegador. Ele suporta múltiplos tipos de operação (ex: 700 - Entrada Spot, 001 - VENDAS), executa tarefas automatizadas a partir de dados, e pode rodar múltiplas threads para testes de estresse e medição de performance. Conta ainda com uma API para ingestão de telemetria.

## Funcionalidades

- Login automatizado
- Preenchimento automático de formulários para diferentes tipos de operação (ex: Entrada Spot, Vendas)
- Baseado em dados: lê informações de operação e login de arquivos JSON ou banco SQLite
- Execução multi-thread para testes de estresse
- Rotinas modulares para cada tipo de operação
- Telemetria e registro de duração de cada etapa
- API FastAPI para telemetria (exporter/)

## Estrutura do Projeto

- `main.py` — Ponto de entrada. Gerencia execução por threads e seleção de rotinas
- `db/` — Arquivos de dados, scripts de carregamento, rotina de telemetria, banco SQLite
- `exporter/` — API FastAPI para recebimento de telemetria
- `routines/` — Rotinas de automação moduladas por operação (ex: operacao_700, pesagem, classificacao)
- `utils/` — Funções utilitárias para Playwright e manipulação de páginas

## Instalação

1. **Clone o repositório:**
   ```bash
   git clone <repo-url>
   cd agro-teste
   ```
2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   pip install fastapi uvicorn
   playwright install  # instala os navegadores suportados
   ```

## Uso

1. **Prepare seus dados:**
   - Edite ou carregue dados no banco SQLite (`db/stress_db`) e/ou nos arquivos `.json` em `db/romaneio_data/` conforme a operação desejada.
   - as tabelas utilizadas são: playwright_routine_user, romaneio_data (para os dados do romaneio), routine_romaneio_data (relaciona dados de um romaneio a uma rotina do playwright a ser executada)
   - Certifique-se de registrar parceiros, motoristas, placas, IDs de campos a serem usados conforme a rotina necessária.
   - Veja exemplos de campos e estrutura em `db/routine.json` e arquivos no diretório de dados.

2. **Execute a automação:**
   ```bash
   python main.py
   ```
   Isso irá disparar a automação de acordo com os dados e rotina configurados.

3. **(Opcional) Execute a API de telemetria:**
   ```bash
   cd exporter
   uvicorn api:app --host 0.0.0.0 --port 8089
   ```
   - Acesse `GET /healthcheck` para ver se a API está viva.
   - Use `POST /telemetry` para enviar dados de telemetria.

## Extensão de Operações

- Para adicionar um novo tipo de operação, basta criar novo script Python dentro de `routines/operacao_<codigo>/` ou uma função dedicada no diretório apropriado, seguindo o modelo das rotinas existentes.
- Para novas rotinas de pesagem ou classificação, consulte `routines/pesagem/` e `routines/classificacao/` respectivamente.

## Configuração

- **Dados de operação e login:**
  - SQLite: `db/stress_db`
  - JSON: arquivos em `db/romaneio_data/`
- **Operações suportadas:**
  - 700 - Entrada Spot
  - 001 - VENDAS
  - 302 - COMPRA
  - (Extensível via adição de rotinas no diretório routines/)

## Dependências

- Python 3.8+
- [Playwright para Python](https://playwright.dev/python/)
- FastAPI e Uvicorn (recomendado para API)
- sqlite3 (biblioteca padrão)

Para instalar manualmente, use:
```bash
pip install playwright fastapi uvicorn
```

## Licença

Este projeto está licenciado sob a Licença MIT.

## Roadmap

- [ ] Adicionar endpoint/api de ingestão de dados diretamente pelo usuário (atualizar rotina de inserts)
- [ ] Implementar persistência de métricas de execução utilizando `save_telemetry.py` via API ou arquivo
