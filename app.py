# app.py (VERSÃO ATUALIZADA COM PRIORIDADES)

from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)

DB_PATH = "tarefas.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(DB_PATH):
        print("Criando banco de dados...")
        conn = get_db_connection()
        conn.execute('''
            CREATE TABLE tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                concluida INTEGER NOT NULL DEFAULT 0,
                prioridade INTEGER NOT NULL DEFAULT 1
            );
        ''')
        conn.commit()
        conn.close()
        print("Banco de dados criado com sucesso.")

@app.route('/')
def index():
    """Renderiza a página principal com a lista de tarefas."""
    conn = get_db_connection()
    # ALTERAÇÃO AQUI: Ordena por prioridade e depois por ID
    tarefas = conn.execute('SELECT * FROM tarefas ORDER BY prioridade DESC, id ASC').fetchall()
    conn.close()
    return render_template('index.html', tarefas=tarefas)

@app.route('/api/tarefas', methods=['POST'])
def adicionar_tarefa():
    """Adiciona uma nova tarefa ao banco de dados, incluindo a prioridade."""
    dados = request.get_json()
    descricao = dados['descricao']
    # ALTERAÇÃO AQUI: Pega a prioridade que virá do front-end.
    prioridade = dados.get('prioridade', 1)

    conn = get_db_connection()
    cursor = conn.cursor()
    # ALTERAÇÃO AQUI: O comando SQL INSERT agora inclui a coluna 'prioridade'
    cursor.execute('INSERT INTO tarefas (descricao, prioridade) VALUES (?, ?)',
                   (descricao, prioridade))
    nova_tarefa_id = cursor.lastrowid
    conn.commit()
    conn.close()

    # ALTERAÇÃO AQUI: Retorna a prioridade na resposta JSON
    return jsonify({'id': nova_tarefa_id, 'descricao': descricao, 'concluida': 0, 'prioridade': prioridade}), 201

@app.route('/api/tarefas/<int:id>/concluir', methods=['PUT'])
def concluir_tarefa(id):
    dados = request.get_json()
    concluida = dados.get('concluida', 0)
    conn = get_db_connection()
    conn.execute('UPDATE tarefas SET concluida = ? WHERE id = ?', (concluida, id))
    conn.commit()
    conn.close()
    return jsonify({'sucesso': True})

@app.route('/api/tarefas/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tarefas WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'sucesso': True})

@app.route('/api/tarefas/<int:id>', methods=['PUT'])
def editar_tarefa(id):
    dados = request.get_json()
    if not dados or 'descricao' not in dados:
        return jsonify({'erro': 'Nova descrição não fornecida'}), 400
    nova_descricao = dados['descricao'].strip()
    if not nova_descricao:
        return jsonify({'erro': 'Descrição não pode ser vazia'}), 400
    conn = get_db_connection()
    tarefa = conn.execute('SELECT * FROM tarefas WHERE id = ?', (id,)).fetchone()
    if tarefa is None:
        conn.close()
        return jsonify({'erro': 'Tarefa não encontrada'}), 404
    conn.execute('UPDATE tarefas SET descricao = ? WHERE id = ?', (nova_descricao, id))
    conn.commit()
    conn.close()
    return jsonify({'sucesso': True, 'descricao': nova_descricao})

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)