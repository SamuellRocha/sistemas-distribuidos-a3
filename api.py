import sqlite3
from sqlite3 import Error
from flask import Flask, request, jsonify
from datetime import date

app = Flask(__name__)

#######################################################
#  1) GET: pesquisar usuários
#######################################################

@app.route('/api-usuarios/usuarios/', methods=['GET'])
@app.route('/api-usuarios/usuarios/<int:id_usuario>', methods=['GET'])
def pesquisar_usuarios(id_usuario=None):
    if request.method == 'GET':
        if id_usuario is not None:
            sql = '''SELECT * FROM usuarios WHERE id = ?'''
        else:
            sql = '''SELECT * FROM usuarios'''

        try:
            conn = sqlite3.connect('database/db-tarefas.db')

            cur = conn.cursor()
            if id_usuario is not None:
                cur.execute(sql, (id_usuario,))
            else:
                cur.execute(sql)
                
            registros = cur.fetchall()

            if registros:
                nomes_colunas = [x[0] for x in cur.description]

                json_dados = []
                for reg in registros:
                    json_dados.append(dict(zip(nomes_colunas, reg)))

                return jsonify(json_dados)
            else:
                return jsonify({'mensagem': 'registro nao encontrado'})

        except Error as e:
            return jsonify({'mensagem': str(e)})
        finally:
            conn.close()


#######################################################
#  2) POST: inserir usuário
#######################################################

@app.route('/api-usuarios/usuarios', methods=['POST'])
def inserir_usuario():
    if request.method == 'POST':
        dados = request.get_json()

        nome = dados.get('nome')
        email = dados.get('email')
        senha = dados.get('senha')
        data_registro = date.today()

        if nome and email and senha:
            registro = (nome, email, senha, data_registro)

            try:
                conn = sqlite3.connect('database/db-tarefas.db')

                sql = ''' INSERT INTO usuarios(nome, email, senha, data_registro) VALUES(?,?,?,?) '''
                cur = conn.cursor()
                cur.execute(sql, registro)
                conn.commit()

                return jsonify({'mensagem': 'registro inserido com sucesso'})

            except Error as e:
                return jsonify({'mensagem': str(e)})
            finally:
                conn.close()

        else:
            return jsonify({'mensagem': 'campos <nome>, <email> e <senha> sao obrigatorios'})


#######################################################
#  3) DELETE: excluir usuário
#######################################################

@app.route('/api-usuarios/usuarios/<int:id_usuario>', methods=['DELETE'])
def excluir_usuario(id_usuario):
    if request.method == 'DELETE':
        if id_usuario:
            try:
                conn = sqlite3.connect('database/db-tarefas.db')

                sql = '''DELETE FROM usuarios WHERE id = ?'''

                cur = conn.cursor()
                cur.execute(sql, (id_usuario,))
                conn.commit()

                return jsonify({'mensagem': 'registro excluido'})

            except Error as e:
                return jsonify({'mensagem': str(e)})
            finally:
                conn.close()
        else:
            return jsonify({'mensagem': 'campo <id_usuario> obrigatorio'})


#######################################################
#  4) PUT: alterar usuário
#######################################################

@app.route('/api-usuarios/usuarios', methods=['PUT'])
def alterar_usuario():
    if request.method == 'PUT':
        dados = request.get_json()

        id_usuario = dados.get('id')
        nome = dados.get('nome')
        email = dados.get('email')
        senha = dados.get('senha')

        if id_usuario and nome and email and senha:
            registro = (nome, email, senha, id_usuario)

            try:
                conn = sqlite3.connect('database/db-tarefas.db')

                sql = ''' UPDATE usuarios SET nome = ?, email = ?, senha = ? WHERE id = ?'''
                cur = conn.cursor()
                cur.execute(sql, registro)
                conn.commit()

                return jsonify({'mensagem': 'registro alterado com sucesso'})

            except Error as e:
                return jsonify({'mensagem': str(e)})
            finally:
                conn.close()

        else:
            return jsonify({'mensagem': 'campos <id>, <nome>, <email> e <senha> sao obrigatorios'})


#######################################################
#  1) GET: pesquisar tarefas
#######################################################

@app.route('/api-tarefas/tarefas/', methods=['GET'])
@app.route('/api-tarefas/tarefas/<int:id_tarefa>', methods=['GET'])
def pesquisar_tarefas(id_tarefa=None):
    if request.method == 'GET':
        if id_tarefa is not None:
            sql = '''SELECT * FROM tarefas WHERE id = ?'''
        else:
            sql = '''SELECT * FROM tarefas'''

        try:
            conn = sqlite3.connect('database/db-tarefas.db')

            cur = conn.cursor()
            if id_tarefa is not None:
                cur.execute(sql, (id_tarefa,))
            else:
                cur.execute(sql)
                
            registros = cur.fetchall()

            if registros:
                nomes_colunas = [x[0] for x in cur.description]

                json_dados = []
                for reg in registros:
                    json_dados.append(dict(zip(nomes_colunas, reg)))

                return jsonify(json_dados)
            else:
                return jsonify({'mensagem': 'registro nao encontrado'})

        except Error as e:
            return jsonify({'mensagem': str(e)})
        finally:
            conn.close()


#######################################################
#  2) POST: inserir tarefa
#######################################################

@app.route('/api-tarefas/tarefas', methods=['POST'])
def inserir_tarefa():
    if request.method == 'POST':
        dados = request.get_json()

        titulo = dados.get('titulo')
        descricao = dados.get('descricao')
        status = dados.get('status')
        prioridade = dados.get('prioridade')
        id_usuario = dados.get('id_usuario')
        data_criacao = date.today()

        if titulo and descricao and status and prioridade and id_usuario:
            registro = (titulo, descricao, data_criacao, status, prioridade, id_usuario)

            try:


                conn = sqlite3.connect('database/db-tarefas.db')        
                sql = ''' INSERT INTO tarefas(titulo, descricao, data_criacao, status, prioridade, id_usuario) VALUES(?,?,?,?,?,?) '''
                cur = conn.cursor()
                cur.execute(sql, registro)
                conn.commit()

                return jsonify({'mensagem': 'registro inserido com sucesso'})

            except Error as e:
                return jsonify({'mensagem': str(e)})
            finally:
                conn.close()
        
        else:
            return jsonify({'mensagem': 'campos <titulo>, <descricao>, <status>, <prioridade> e <id_usuario> sao obrigatorios'})


#######################################################
#  3) DELETE: excluir tarefa
#######################################################

@app.route('/api-tarefas/tarefas/<int:id_tarefa>', methods=['DELETE'])
def excluir_tarefa(id_tarefa):
    if request.method == 'DELETE':
        if id_tarefa:
            try:
                conn = sqlite3.connect('database/db-tarefas.db')

                sql = '''DELETE FROM tarefas WHERE id = ?'''

                cur = conn.cursor()
                cur.execute(sql, (id_tarefa,))
                conn.commit()

                return jsonify({'mensagem': 'registro excluido'})

            except Error as e:
                return jsonify({'mensagem': str(e)})
            finally:
                conn.close()
        else:
            return jsonify({'mensagem': 'campo <id_tarefa> obrigatorio'})


#######################################################
#  4) PUT: alterar tarefa
#######################################################

@app.route('/api-tarefas/tarefas', methods=['PUT'])
def alterar_tarefa():
    if request.method == 'PUT':
        dados = request.get_json()

        id_tarefa = dados.get('id')
        titulo = dados.get('titulo')
        descricao = dados.get('descricao')
        status = dados.get('status')
        prioridade = dados.get('prioridade')
        id_usuario = dados.get('id_usuario')

        if id_tarefa and titulo and descricao and status and prioridade and id_usuario:
            registro = (titulo, descricao, status, prioridade, id_usuario, id_tarefa)

            try:
                conn = sqlite3.connect('database/db-tarefas.db')

                sql = ''' UPDATE tarefas SET titulo = ?, descricao = ?, status = ?, prioridade = ?, id_usuario = ? WHERE id = ?'''
                cur = conn.cursor()
                cur.execute(sql, registro)
                conn.commit()

                return jsonify({'mensagem': 'registro alterado com sucesso'})

            except Error as e:
                return jsonify({'mensagem': str(e)})
            finally:
                conn.close()

        else:
            return jsonify({'mensagem': 'campos <id>, <titulo>, <descricao>, <status>, <prioridade> e <id_usuario> sao obrigatorios'})


#######################################################
# 5) UrlPoint nao localizado
#######################################################

@app.errorhandler(404)
def endpoint_nao_encontrado(e):
    return jsonify({'mensagem': 'erro - endpoint nao encontrado'}), 404

@app.errorhandler(405)
def metodo_nao_permitido(e):
    return jsonify({'mensagem': 'erro - método nao permitido'}), 405


#######################################################
# XX Execucao da Aplicacao
#######################################################

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
