import sqlite3

def criar_banco():
    with open('db/schema.sql', 'r', encoding='utf-8') as f:  # Lê o conteúdo do arquivo schema.sql
        schema = f.read()
    conn = sqlite3.connect('db/financeiro.db')           # Cria uma conexão com o banco de dados chamado 'financeiro.db'
    cursor = conn.cursor()                               # Cria um cursor, que permite executar comandos SQL no banco
    cursor.executescript(schema)                         # Executa o conteúdo do script SQL na conexão do banco
    conn.commit()                                        # Salva as alterações (neste caso, a criação das tabelas)
    conn.close()                                         # Fecha a conexão com o banco de dados
    print("Banco de dados criado com sucesso!")

if __name__ == '__main__':
    criar_banco()
