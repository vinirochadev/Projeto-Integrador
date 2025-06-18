from flask import Flask, render_template, request, redirect, flash
from datetime import datetime
from services.transacoes_service import listar_transacoes, adicionar_transacao, calcular_totais, excluir_transacao
from models.transacao import Transacao
import os

# Inicializa a aplicação Flask
app = Flask(__name__)
# Chave secreta para uso de sessões e flash
app.secret_key = 'minha-chave-super-secreta-123'

# Rota principal: exibe o dashboard e lista de transações
@app.route("/")
def index():
    # Obtém filtros da query string
    tipo = request.args.get("tipo", "")
    data_inicio = request.args.get("data_inicio", "")
    data_fim = request.args.get("data_fim", "")

    # Busca transações e totais filtrados
    transacoes = listar_transacoes(tipo, data_inicio, data_fim)
    totais = calcular_totais(None if tipo == "" else tipo, data_inicio or None, data_fim or None)
    saldo = totais["receita"] - totais["despesa"]

    # Renderiza o template principal
    return render_template(
        "index.html",
        transacoes=transacoes,
        tipo=tipo,
        data_inicio=data_inicio,
        data_fim=data_fim,
        totais=totais,
        saldo=saldo
    )

# Rota para adicionar uma nova transação
@app.route("/adicionar", methods=["POST"])
def adicionar():
    descricao = request.form["descricao"]
    valor_str = request.form["valor"].replace("R$ ", "").replace(" ", "").replace(".", "").replace(",", ".")
    try:
        valor = float(valor_str)
    except ValueError:
        flash("Valor inválido! Digite apenas números no campo Valor.", "error")
        return redirect("/")
    if valor <= 0:
        flash("O valor deve ser maior que zero.", "error")
        return redirect("/")
    data_str = request.form["data"]
    tipo = request.form["tipo"]
    try:
        # Converte de "DD/MM/AAAA" para "AAAA-MM-DD"
        data_formatada = datetime.strptime(data_str, "%d/%m/%Y").strftime("%Y-%m-%d")
    except ValueError:
        flash("Data inválida! Use o formato DD/MM/AAAA.", "error")
        return redirect("/")

    # Cria e salva a nova transação
    nova_transacao = Transacao(None, descricao, valor, data_formatada, tipo)
    adicionar_transacao(nova_transacao)

    return redirect("/")

# Rota para excluir uma transação pelo id
@app.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):
    excluir_transacao(id)
    flash("Transação excluída com sucesso!", "success")
    return redirect("/")

# Executa a aplicação em modo debug se for o arquivo principal
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
