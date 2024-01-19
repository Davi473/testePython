import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Criação de uma conexão com o banco de dados SQLite (ou cria um novo se não existir)
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# Criação de uma tabela simples
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
    )
''')
conn.commit()

# Rota para adicionar um novo usuário
@app.route('/adicionar_usuario', methods=['POST'])
def adicionar_usuario():
    dados_usuario = request.json
    nome = dados_usuario['nome']
    idade = dados_usuario['idade']

    # Inserção do usuário na tabela
    cursor.execute('INSERT INTO usuarios (nome, idade) VALUES (?, ?)', (nome, idade))
    conn.commit()

    return jsonify({"mensagem": "Usuário adicionado com sucesso"})

# Rota para obter todos os usuários
@app.route('/obter_usuarios', methods=['GET'])
def obter_usuarios():
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    return jsonify({"usuarios": usuarios})

# Execução do servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
