# Controle de Documentos - Projeto Integrador II, Módulo 3

Modelo demonstrativo de banco de dados relacional para controle de solicitações documentais no contexto de escritório de advocacia.

## Escopo e continuidade

Esta etapa apresenta a modelagem e a manipulação de dados com SQLite e o registro da versão inicial do projeto no GitHub. O banco de dados demonstrativo não está integrado ao `index.html` da etapa anterior. A aplicação web original permanece como protótipo com armazenamento em `localStorage`, e o código dessa interface não integra este repositório.

## Entidades e relacionamento

- `atendimentos`: `id` (chave primária), `cliente`, `referencia`.
- `solicitacoes_documentais`: `id` (chave primária), `atendimento_id` (chave estrangeira), `documento`, `data_solicitacao`, `recebido` (0/1).
- Relacionamento: um atendimento pode ter diversas solicitações documentais (1:N).
- Regras de integridade: nomes não vazios, `recebido` apenas 0 ou 1 e vínculo com `atendimento_id` existente.

Diagrama: `evidencias/diagrama_er.png`; fonte editável: `diagrama_er.dot`.

## Arquivos SQL

- `sql/01_esquema.sql`: criação das tabelas, restrições `CHECK`, `FOREIGN KEY` e índice.
- `sql/02_dados_ficticios.sql`: inserção de dois atendimentos e três solicitações fictícias.
- `sql/03_operacoes.sql`: exemplos de `SELECT` com `JOIN`, `UPDATE` e `DELETE`.

## Verificação reproduzível

É necessário ter Python 3, que já inclui o módulo `sqlite3` na biblioteca padrão. Na pasta do projeto, execute:

```bash
python3 tests/executar_demonstracao.py
```

O programa recria o banco SQLite demonstrativo, executa o esquema e as operações SQL, verifica os resultados e as restrições de integridade e produz `evidencias/resultado_testes.txt`.

## Git e publicação

Os arquivos foram organizados e publicados na branch principal (`main`) de um repositório público no GitHub. A publicação inicial foi realizada por meio de um commit, reunindo os scripts SQL, o programa de verificação, o diagrama e a documentação deste módulo.

Esse registro identifica a versão inicial disponibilizada e serve como referência para alterações futuras. A continuidade do projeto poderá ser acompanhada por novos commits e, quando necessário, por branches destinadas a mudanças específicas.

Repositório: https://github.com/mairaribeiro15/Relat-rio-Banco-de-Dados-e-Controle-de-Vers-o

## Limitações

Trata-se de exercício acadêmico com dados fictícios. Não há autenticação, servidor web, sincronização, cópia de segurança nem integração da interface com o banco SQL. O projeto não deve ser utilizado com dados reais de clientes.
