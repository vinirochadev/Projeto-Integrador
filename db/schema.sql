DROP TABLE IF EXISTS transacoes;

CREATE TABLE transacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    valor REAL NOT NULL,
    data TEXT NOT NULL,
    tipo TEXT NOT NULL  -- "receita" ou "despesa"
);
