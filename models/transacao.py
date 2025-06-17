# Classe que representa uma transação financeira (receita ou despesa)
class Transacao:
    def __init__(self, id, descricao, valor, data, tipo):
        # Identificador da transação
        self.id = id
        # Descrição da transação (ex: "Salário", "Aluguel", "Supermercado")
        self.descricao = descricao

        # Valor numérico da transação (positivo, mesmo para despesas)
        self.valor = valor

        # Data da transação (formato "AAAA-MM-DD")
        self.data = data

        # Tipo da transação: "receita" ou "despesa"
        self.tipo = tipo