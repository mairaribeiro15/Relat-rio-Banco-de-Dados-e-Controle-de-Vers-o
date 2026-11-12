INSERT INTO atendimentos (cliente, referencia)
VALUES ('Cliente Ficticio A', 'Atendimento 001');

INSERT INTO atendimentos (cliente, referencia)
VALUES ('Cliente Ficticio B', 'Atendimento 002');

INSERT INTO solicitacoes_documentais
    (atendimento_id, documento, data_solicitacao)
VALUES
    (1, 'Procuracao assinada', '2026-11-03'),
    (1, 'Documento de identificacao', '2026-11-03'),
    (2, 'Comprovante de endereco', '2026-11-03');
