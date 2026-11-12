#!/usr/bin/env python3
"""Reproduce a SQLite-only demonstration with fictitious data."""
from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parents[1]
EVID = ROOT / "evidencias"
EVID.mkdir(parents=True, exist_ok=True)
DB = EVID / "controle_documentos_demo.sqlite"
if DB.exists():
    DB.unlink()

with sqlite3.connect(DB) as db:
    db.execute("PRAGMA foreign_keys = ON")
    db.executescript((ROOT / "sql/01_esquema.sql").read_text(encoding="utf-8"))
    db.executescript((ROOT / "sql/02_dados_ficticios.sql").read_text(encoding="utf-8"))
    assert db.execute("SELECT COUNT(*) FROM atendimentos").fetchone()[0] == 2
    assert db.execute("SELECT COUNT(*) FROM solicitacoes_documentais").fetchone()[0] == 3

    inicial = db.execute("""
        SELECT a.cliente, s.documento, s.recebido
        FROM atendimentos a
        JOIN solicitacoes_documentais s ON s.atendimento_id=a.id
        ORDER BY a.id, s.id
    """).fetchall()
    assert len(inicial) == 3

    db.executescript((ROOT / "sql/03_operacoes.sql").read_text(encoding="utf-8"))
    final = db.execute("""
        SELECT a.cliente, s.documento, s.recebido
        FROM atendimentos a
        JOIN solicitacoes_documentais s ON s.atendimento_id=a.id
        ORDER BY a.id, s.id
    """).fetchall()
    assert len(final) == 2
    assert db.execute("SELECT COUNT(*) FROM solicitacoes_documentais WHERE recebido=1").fetchone()[0] == 1
    assert db.execute("SELECT COUNT(*) FROM solicitacoes_documentais WHERE recebido=0").fetchone()[0] == 1

    fk_rejeitada = False
    try:
        db.execute("INSERT INTO solicitacoes_documentais (atendimento_id, documento) VALUES (999, 'Registro invalido')")
    except sqlite3.IntegrityError:
        fk_rejeitada = True
    assert fk_rejeitada

    status_rejeitado = False
    try:
        db.execute("UPDATE solicitacoes_documentais SET recebido=2 WHERE id=1")
    except sqlite3.IntegrityError:
        status_rejeitado = True
    assert status_rejeitado
    db.rollback()

linhas = [
    "DEMONSTRACAO LOCAL SQLITE - PITI II / MODULO 3",
    "Execucao: banco SQLite criado somente com dados ficticios",
    "Tabelas: atendimentos (2 registros), solicitacoes_documentais (3 inseridos)",
    "Operacoes executadas: CREATE TABLE, INSERT, SELECT com JOIN, UPDATE, DELETE",
    "Antes das operacoes: " + str(inicial),
    "Depois das operacoes: " + str(final),
    "Verificacao final: 2 solicitacoes, sendo 1 recebida e 1 pendente",
    "Integridade: FK invalida rejeitada = " + str(fk_rejeitada),
    "Integridade: status fora de 0/1 rejeitado = " + str(status_rejeitado),
    "Resultado: verificacoes automaticas passaram",
    "Nao comprova integracao com aplicacao web ou publicacao no GitHub.",
]
texto = "\n".join(linhas) + "\n"
(EVID / "resultado_testes.txt").write_text(texto, encoding="utf-8")
print(texto)
