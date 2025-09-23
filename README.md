# Automação Agro Teste

## Descrição

Este projeto automatiza o processo de preenchimento e envio de romaneios utilizando o Playwright para automação de navegador. Ele suporta múltiplos tipos de operação (ex: 700 - Entrada Spot, 001 - VENDAS) e pode rodar múltiplas threads para testes de estresse e medição de performance. O projeto foi desenvolvido para automação robusta, repetível e baseada em dados.

## Funcionalidades

- Login automatizado
- Preenchimento automático de formulários para diferentes tipos de operação (ex: Entrada Spot, Vendas)
- Baseado em dados: lê informações de operação e login de arquivos JSON ou banco SQLite
- Execução multi-thread para testes de estresse
- Rotinas modulares para cada tipo de operação
- Telemetria e registro de duração de cada etapa

## Estrutura do Projeto

- `main.py` — Ponto de entrada, gerencia threads e seleção de rotinas
- `db/` — Contém arquivos de dados, banco de dados e scripts de carregamento
- `repository/` — Utilitários de conexão com banco de dados
- `routines/` — Rotinas de automação para cada tipo de operação
- `utils/` — Funções utilitárias para Playwright e interação com páginas

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
   pip install playwright
   pip install -r requirements.txt
   playwright install  # Instala os navegadores
   ```

## Uso

1. **Prepare seus dados:**
   - Fazer um selecct no banco de dados selecionando:
        - 1 parceiro
        - 1 motorista
        - N placas e seu reboque 1
        - Inspecione o elemento das operacoes e obtenha:
            - btn_salvar_id = id do elemento do botao salvar
            - btn_incluir_item_nf_pedido = id do elemento do botao de incluir item
            - parceiro_input_id = id do campo de parceiro
            - parceiro_ul_id = id da tabela de autocomplete
            - transportadora_input_id = id do campo de preenchimento da transportadora
            - transportadora_ul_id = id da tabela de autocomplete do campo transportadora
        - Crie inserts na romaneio_data, substituindo com os valores desejados acima


    Sendo N o numero de romaneios que voce deseja criar
2. **Execute a automação:**
   ```bash
   python main.py
   ```

## Exemplo

```python
python main.py
```

## Configuração

- **Dados de operação e login:**
  - SQLite: `db/stress_db`
- **Operações suportadas:**
  - 700 - Entrada Spot
  - 001 - VENDAS
  - 302 - COMPRA
  - (Extensível via adicao de routines/operacao_xxx/)

## Dependências

- Python 3.8+
- [Playwright para Python](https://playwright.dev/python/)
- sqlite3 (biblioteca padrão)

## Licença

Este projeto está licenciado sob a Licença MIT.

## Roadmap

- [ ] Adicionar um endpoint (API) que receba os dados descritos na seção "Prepare seus dados" e realize inserts no banco de dados.
- [ ] Implementar persistência de métricas de execução utilizando o módulo `save_telemetry.py`.
