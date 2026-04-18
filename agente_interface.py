import streamlit as st
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()

# 1. Título na página Web
st.title(" ⛽ Assistente de Segurança da Petrobras")
st.write("Faça sua pergunta para o Assistente de Segurança da Petrobras!")

# 2. Carregando o agente (Usamos @st.cache_resource para ele não recriar o banco de dados a cada clique)
@st.cache_resource
def iniciar_agente():
    banco = SqliteDb(db_file="tmp/busca.db")
    return Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        description="Você é um especialista em segurança no trabalho. Você é responsável por monitorar operações com guindastes na Petrobras. Você responde solicitações dos operadores novatos e que possuem dúvidas em relação a segurança. Você responde com um tom técnico, porém, pensando que existem operadores com diferentes níveis de instrução acadêmica.",
        db=banco,
        add_history_to_context=True,
        num_history_runs=3,
        tools=[DuckDuckGoTools()],
        markdown=True
    )

agente = iniciar_agente()

# 3. Substituindo o "input()" e o "while True" do terminal:
mensagem = st.chat_input("Qual a sua solicitação, Operador? 👷")

if mensagem:
    # Mostra o que o usuário digitou na tela
    with st.chat_message("user"):
        st.write(mensagem)

    # Faz a IA pensar, pesquisar e responder
    with st.chat_message("assistant"):
        with st.spinner("Pesquisando na base de conhecimento e dados da empresa Petrobras"):
            
            # A IA recebe a mensagem e a 'chave da memória' ao mesmo tempo
            resposta = agente.run(
                mensagem
            )
            
            st.write(resposta.content)