import sqlite3
from models.transacao import Transacao  # Classe que representa uma transação financeira

# Cria e retorna uma conexão com o banco de dados SQLite
def obter_conexao():
    conn = sqlite3.connect('db/financeiro.db')
    conn.row_factory = sqlite3.Row  # Permite acessar colunas por nome
    return conn

# Adiciona uma nova transação ao banco de dados
# Recebe um objeto Transacao
def adicionar_transacao(transacao: Transacao):
    conn = obter_conexao()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO transacoes (descricao, valor, data, tipo)
        VALUES (?, ?, ?, ?)
    """, (transacao.descricao, transacao.valor, transacao.data, transacao.tipo))
    conn.commit()
    conn.close()

# Lista transações, podendo filtrar por tipo e intervalo de datas
# Retorna uma lista de objetos Transacao
def listar_transacoes(tipo=None, data_inicio=None, data_fim=None):
    conn = obter_conexao()
    cursor = conn.cursor()

    query = "SELECT * FROM transacoes WHERE 1=1"
    params = []

    if tipo:
        query += " AND tipo = ?"
        params.append(tipo)

    if data_inicio:
        query += " AND date(data) >= date(?)"
        params.append(data_inicio)

    if data_fim:
        query += " AND date(data) <= date(?)"
        params.append(data_fim)

    query += " ORDER BY date(data) ASC"
    cursor.execute(query, params)
    linhas = cursor.fetchall()
    conn.close()
    return [Transacao(linha['id'], linha['descricao'], linha['valor'], linha['data'], linha['tipo']) for linha in linhas]

# Calcula o total de receitas e despesas, podendo filtrar por tipo e datas
# Retorna um dicionário: {"receita": valor, "despesa": valor}
def calcular_totais(tipo=None, data_inicio=None, data_fim=None):
    conn = obter_conexao()
    cursor = conn.cursor()

    base_query = "SELECT tipo, SUM(valor) as total FROM transacoes WHERE 1=1"
    params = []

    if tipo:
        base_query += " AND tipo = ?"
        params.append(tipo)
    if data_inicio:
        base_query += " AND date(data) >= date(?)"
        params.append(data_inicio)
    if data_fim:
        base_query += " AND date(data) <= date(?)"
        params.append(data_fim)

    base_query += " GROUP BY tipo"
    cursor.execute(base_query, params)

    totais = {"receita": 0.0, "despesa": 0.0}
    for linha in cursor.fetchall():
        if linha["tipo"] == "receita":
            totais["receita"] = linha["total"]
        elif linha["tipo"] == "despesa":
            totais["despesa"] = linha["total"]

    conn.close()
    return totais

# Exclui uma transação do banco de dados pelo id
# Recebe o id da transação a ser removida
def excluir_transacao(id):
    conn = obter_conexao()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transacoes WHERE id = ?", (id,))
    conn.commit()
    conn.close()
