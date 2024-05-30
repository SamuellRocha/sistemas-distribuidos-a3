import sqlite3
from sqlite3 import Error

def criar_tabelas():
    conn = None  # Inicialize a variável conn antes do bloco try
    try:
        conn = sqlite3.connect('database/db-tarefas.db')
        
        sql_create_usuarios = '''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            senha TEXT NOT NULL,
            data_registro DATE NOT NULL
        );
        '''
        
        sql_create_tarefas = '''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT NOT NULL,
            data_criacao DATE NOT NULL,
            status TEXT NOT NULL,
            prioridade TEXT NOT NULL,
            id_usuario INTEGER NOT NULL,
            FOREIGN KEY (id_usuario) REFERENCES usuarios (id)
        );
        '''
        
        cur = conn.cursor()
        cur.execute(sql_create_usuarios)
        cur.execute(sql_create_tarefas)
        conn.commit()
        print("Tabelas 'usuarios' e 'tarefas' criadas com sucesso")
    except Error as e:
        print(f"Erro ao criar tabelas: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    criar_tabelas()
