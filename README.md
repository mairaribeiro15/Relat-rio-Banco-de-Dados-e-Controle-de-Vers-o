# Controle de Documentos - Projeto Integrador II, Módulo 3

Modelo demonstrativo de banco de dados relacional para controle de solicitações documentais no contexto de escritório de advocacia.

## Escopo e continuidade

Esta etapa apresenta a modelagem e manipulação de dados usando SQLite, além de um histórico local de controle de versão com Git. **O banco demonstrativo não está integrado ao `index.html` da etapa anterior.** A aplicação web original permanece descrita como protótipo com `localStorage`. O código original dessa interface não integra este pacote.

## Entidades e relacionamento

- `atendimentos`: `id` (chave primária), `cliente`, `referencia`.
- `solicitacoes_documentais`: `id` (chave primária), `atendimento_id` (chave estrangeira), `documento`, `data_solicitacao`, `recebido` (0/1).
- Relacionamento: um atendimento pode ter diversas solicitações.
- Regras: nomes não vazios, `recebido` apenas 0 ou 1 e `atendimento_id` existente.

Diagrama: `evidencias/diagrama_er.png`; fonte editável: `diagrama_er.dot`.

## Arquivos SQL

- `sql/01_esquema.sql`: tabelas, `CHECK`, `FOREIGN KEY` e índice.
- `sql/02_dados_ficticios.sql`: inserção de dois atendimentos e três solicitações fictícias.
- `sql/03_operacoes.sql`: exemplos de `SELECT` com `JOIN`, `UPDATE` e `DELETE`.

## Verificação reproduzível

Requer Python 3 com módulo `sqlite3` (biblioteca padrão). Na pasta do projeto, execute:

```sh
python3 tests/executar_demonstracao.py
```

O programa recria o banco SQLite demonstrativo, executa o esquema e as operações SQL, testa as contagens e algumas restrições de integridade e produz `evidencias/resultado_testes.txt`.

## Git e publicação

O projeto foi publicado em um repositório público no GitHub, reunindo os scripts SQL, o diagrama relacional, o programa de verificação e a documentação.

A versão apresentada nesta etapa foi registrada por meio de um commit inicial na branch principal (main). Esse registro permite consultar os arquivos disponibilizados e estabelece uma referência para futuras modificações.

O histórico de versionamento poderá ser ampliado nas próximas etapas do desenvolvimento, com novos commits descritivos e, conforme a necessidade, a utilização de branches para organizar alterações específicas.
## Limitações

Trata-se de exercício acadêmico com dados fictícios. Não há autenticação, servidor web, sincronização, cópia de segurança nem integração da interface com o banco SQL. Não utilizar com dados reais de clientes.
