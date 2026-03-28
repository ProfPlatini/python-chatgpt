import streamlit as st
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()

# 1. Título na página Web
st.title("🔎 Assistente de Pesquisa com IA")
st.write("Faça uma pergunta e eu vou buscar na internet para você!")

# 2. Carregando o agente (Usamos @st.cache_resource para ele não recriar o banco de dados a cada clique)
@st.cache_resource
def iniciar_agente():
    banco = SqliteDb(db_file="tmp/busca.db")
    return Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        description="Você é um assistente de pesquisa. Responda em português.",
        db=banco,
        add_history_to_context=True,
        num_history_runs=3,
        tools=[DuckDuckGoTools()],
        markdown=True
    )

agente = iniciar_agente()

# 3. Substituindo o "input()" e o "while True" do terminal:
mensagem = st.chat_input("Digite a sua pergunta:")

if mensagem:
    # Mostra o que o usuário digitou na tela
    with st.chat_message("user"):
        st.write(mensagem)

    # Faz a IA pensar, pesquisar e responder
    with st.chat_message("assistant"):
        with st.spinner("Pesquisando na internet..."):
            
            # A IA recebe a mensagem e a 'chave da memória' ao mesmo tempo
            resposta = agente.run(
                mensagem, 
                session_id="82819c16-6a52-4bc6-b91b-31bf50f74545" ##Fzer na segunda vez com eles 
            )
            
            st.write(resposta.content)