import sqlite3
from sqlite3 import Error
from datetime import date

def inserir_exemplos():
    try:
        conn = sqlite3.connect('database/db-tarefas.db')
        
        usuarios_exemplos = [
            ('Alice Silva', 'alice@example.com', 'senha123', date.today()),
            ('Bob Santos', 'bob@example.com', 'senha456', date.today()),
            ('Carlos Oliveira', 'carlos@example.com', 'senha789', date.today())
        ]
        
        tarefas_exemplos = [
            ('Finalizar relatório', 'Concluir o relatório financeiro do Q1', date.today(), 'Pendente', 'Alta', 1),
            ('Reunião com a equipe', 'Reunião semanal com a equipe de desenvolvimento', date.today(), 'Concluída', 'Média', 1),
            ('Planejamento de marketing', 'Criar o plano de marketing para o novo produto', date.today(), 'Em Progresso', 'Alta', 2),
            ('Atualizar site', 'Implementar as novas atualizações no site corporativo', date.today(), 'Pendente', 'Baixa', 3),
            ('Feedback dos clientes', 'Coletar e analisar feedbacks dos clientes', date.today(), 'Concluída', 'Média', 2)
        ]
        
        sql_insert_usuarios = '''
        INSERT INTO usuarios (nome, email, senha, data_registro)
        VALUES (?, ?, ?, ?)
        '''
        
        sql_insert_tarefas = '''
        INSERT INTO tarefas (titulo, descricao, data_criacao, status, prioridade, id_usuario)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
        
        cur = conn.cursor()
        cur.executemany(sql_insert_usuarios, usuarios_exemplos)
        cur.executemany(sql_insert_tarefas, tarefas_exemplos)
        conn.commit()
        print("Exemplos inseridos com sucesso")
    except Error as e:
        print(f"Erro ao inserir exemplos: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    inserir_exemplos()
