import streamlit as st
import requests

# Configurações da API
API_URL = "http://100.24.51.252:8080"

# Títulos da aplicação
st.title("Gerenciamento de Usuários e Tarefas")

# Seleção de opções
opcao = st.sidebar.selectbox(
    "Escolha uma opção",
    ("Pesquisar Usuários", "Inserir Usuário", "Alterar Usuário", "Excluir Usuário",
     "Pesquisar Tarefas", "Inserir Tarefa", "Alterar Tarefa", "Excluir Tarefa")
)

# Funções para consumir a API
def pesquisar_usuarios(id_usuario=None):
    url = f"{API_URL}/api-usuarios/usuarios/"
    if id_usuario:
        url += str(id_usuario)
    response = requests.get(url)
    return response.json()

def inserir_usuario(nome, email, senha):
    url = f"{API_URL}/api-usuarios/usuarios"
    dados = {"nome": nome, "email": email, "senha": senha}
    response = requests.post(url, json=dados)
    return response.json()

def alterar_usuario(id_usuario, nome, email, senha):
    url = f"{API_URL}/api-usuarios/usuarios"
    dados = {"id": id_usuario, "nome": nome, "email": email, "senha": senha}
    response = requests.put(url, json=dados)
    return response.json()

def excluir_usuario(id_usuario):
    url = f"{API_URL}/api-usuarios/usuarios/{id_usuario}"
    response = requests.delete(url)
    return response.json()

def pesquisar_tarefas(id_tarefa=None):
    url = f"{API_URL}/api-tarefas/tarefas/"
    if id_tarefa:
        url += str(id_tarefa)
    response = requests.get(url)
    return response.json()

def inserir_tarefa(titulo, descricao, status, prioridade, id_usuario):
    url = f"{API_URL}/api-tarefas/tarefas"
    dados = {"titulo": titulo, "descricao": descricao, "status": status, "prioridade": prioridade, "id_usuario": id_usuario}
    response = requests.post(url, json=dados)
    return response.json()

def alterar_tarefa(id_tarefa, titulo, descricao, status, prioridade, id_usuario):
    url = f"{API_URL}/api-tarefas/tarefas"
    dados = {"id": id_tarefa, "titulo": titulo, "descricao": descricao, "status": status, "prioridade": prioridade, "id_usuario": id_usuario}
    response = requests.put(url, json=dados)
    return response.json()

def excluir_tarefa(id_tarefa):
    url = f"{API_URL}/api-tarefas/tarefas/{id_tarefa}"
    response = requests.delete(url)
    return response.json()

# Interface para as operações
if opcao == "Pesquisar Usuários":
    st.header("Pesquisar Usuários")
    id_usuario = st.text_input("ID do Usuário (deixe em branco para todos)")
    if st.button("Pesquisar"):
        resultado = pesquisar_usuarios(id_usuario if id_usuario else None)
        st.json(resultado)

elif opcao == "Inserir Usuário":
    st.header("Inserir Usuário")
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    senha = st.text_input("Senha")
    if st.button("Inserir"):
        resultado = inserir_usuario(nome, email, senha)
        st.json(resultado)

elif opcao == "Alterar Usuário":
    st.header("Alterar Usuário")
    id_usuario = st.text_input("ID do Usuário")
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    senha = st.text_input("Senha")
    if st.button("Alterar"):
        resultado = alterar_usuario(id_usuario, nome, email, senha)
        st.json(resultado)

elif opcao == "Excluir Usuário":
    st.header("Excluir Usuário")
    id_usuario = st.text_input("ID do Usuário")
    if st.button("Excluir"):
        resultado = excluir_usuario(id_usuario)
        st.json(resultado)

elif opcao == "Pesquisar Tarefas":
    st.header("Pesquisar Tarefas")
    id_tarefa = st.text_input("ID da Tarefa (deixe em branco para todas)")
    if st.button("Pesquisar"):
        resultado = pesquisar_tarefas(id_tarefa if id_tarefa else None)
        st.json(resultado)

elif opcao == "Inserir Tarefa":
    st.header("Inserir Tarefa")
    titulo = st.text_input("Título")
    descricao = st.text_input("Descrição")
    status = st.text_input("Status")
    prioridade = st.text_input("Prioridade")
    id_usuario = st.text_input("ID do Usuário")
    if st.button("Inserir"):
        resultado = inserir_tarefa(titulo, descricao, status, prioridade, id_usuario)
        st.json(resultado)

elif opcao == "Alterar Tarefa":
    st.header("Alterar Tarefa")
    id_tarefa = st.text_input("ID da Tarefa")
    titulo = st.text_input("Título")
    descricao = st.text_input("Descrição")
    status = st.text_input("Status")
    prioridade = st.text_input("Prioridade")
    id_usuario = st.text_input("ID do Usuário")
    if st.button("Alterar"):
        resultado = alterar_tarefa(id_tarefa, titulo, descricao, status, prioridade, id_usuario)
        st.json(resultado)

elif opcao == "Excluir Tarefa":
    st.header("Excluir Tarefa")
    id_tarefa = st.text_input("ID da Tarefa")
    if st.button("Excluir"):
        resultado = excluir_tarefa(id_tarefa)
        st.json(resultado)

# Executar a aplicação com o comando:
# streamlit run cliente.py
