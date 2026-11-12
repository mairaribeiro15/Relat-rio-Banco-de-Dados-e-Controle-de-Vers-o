PRAGMA foreign_keys = ON;

-- SELECT: situacao dos documentos por atendimento.
SELECT a.cliente, s.documento, s.data_solicitacao, s.recebido
FROM atendimentos AS a
JOIN solicitacoes_documentais AS s ON s.atendimento_id = a.id
ORDER BY a.id, s.id;

-- UPDATE: marcar a primeira solicitacao como recebida.
UPDATE solicitacoes_documentais SET recebido = 1 WHERE id = 1;

-- DELETE: remover a terceira solicitacao ficticia.
DELETE FROM solicitacoes_documentais WHERE id = 3;

-- SELECT: identificar o que ainda esta pendente.
SELECT a.cliente, s.documento
FROM atendimentos AS a
JOIN solicitacoes_documentais AS s ON s.atendimento_id = a.id
WHERE s.recebido = 0
ORDER BY a.cliente, s.documento;
