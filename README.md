# Controle Financeiro

Sistema web para controle de receitas e despesas, desenvolvido em Flask, com interface moderna, responsiva e modo escuro.

## Funcionalidades

- Cadastro de transações (Receita ou Despesa)
- Máscara de valor em tempo real (formato brasileiro)
- Listagem de transações com valores formatados
- Exclusão de transações com confirmação
- Resumo financeiro (Receitas, Despesas, Saldo)
- Filtros por tipo e data (opcional)
- Modo escuro/claro
- Validação de campos e feedback visual

## Tecnologias utilizadas

- Python 3.x
- Flask
- SQLite
- HTML5, CSS3 (moderno, responsivo)
- JavaScript (máscara de valor, interações)
- Font Awesome (ícones)

## Como rodar o projeto

1. **Clone o repositório:**
   ```bash
   git clone <url-do-seu-repositorio>
   cd <nome-da-pasta>
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install flask
   ```

4. **Crie o banco de dados:**
   ```bash
   cd controle_financeiro
   python criar_banco.py
   cd ..
   ```

5. **Execute a aplicação:**
   ```bash
   cd controle_financeiro
   python app.py
   ```

6. **Acesse no navegador:**
   ```
   http://localhost:5000
   ```

## Estrutura do projeto

```
controle_financeiro/
├── app.py
├── criar_banco.py
├── db/
│   ├── financeiro.db
│   └── schema.sql
├── models/
│   └── transacao.py
├── services/
│   └── transacoes_service.py
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   └── layout.html
```

## Observações

- O sistema impede cadastro de transações sem valor.
- O valor é formatado automaticamente para o padrão brasileiro.
- Para excluir uma transação, clique no ícone de lixeira ao lado da transação.
- O modo escuro pode ser alternado no topo direito da tela. 
