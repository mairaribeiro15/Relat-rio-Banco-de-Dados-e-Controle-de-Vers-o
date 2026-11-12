PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS atendimentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente TEXT NOT NULL CHECK (length(trim(cliente)) > 0),
    referencia TEXT
);

CREATE TABLE IF NOT EXISTS solicitacoes_documentais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    atendimento_id INTEGER NOT NULL,
    documento TEXT NOT NULL CHECK (length(trim(documento)) > 0),
    data_solicitacao TEXT NOT NULL DEFAULT (date('now')),
    recebido INTEGER NOT NULL DEFAULT 0 CHECK (recebido IN (0, 1)),
    FOREIGN KEY (atendimento_id)
        REFERENCES atendimentos(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE INDEX IF NOT EXISTS idx_solicitacoes_atendimento
    ON solicitacoes_documentais (atendimento_id);
