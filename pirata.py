import streamlit as st
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="O Capitão da IA", page_icon="🏴‍☠️")

st.title("🏴‍☠️ O Capitão dos Sete Mares")
st.subheader("Benvindo a bordo, marujo! O que buscas nos confins da internet? 🌊")
st.divider()

@st.cache_resource
def iniciar_agente():
    return Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        description=(
            "Você é o Capitão Barba-Código, um pirata veterano que navega pelos sete mares da internet. "
            "Você fala como um pirata (use termos como 'Arrr!', 'Marujo', 'Âncoras ao mar'). "
            "Responda sempre em português com muitos emojis de pirata e mar."
        ),
        tools=[DuckDuckGoTools()],
        markdown=True
    )

agente = iniciar_agente()

mensagem = st.chat_input("Diga ao Capitão o que procurar, marujo...")

if mensagem:
    with st.chat_message("user", avatar="🧑‍💻"):
        st.write(mensagem)

    with st.chat_message("assistant", avatar="🏴‍☠️"):
        with st.spinner("Consultando os mapas náuticos... 🗺️"):
            resposta = agente.run(mensagem)
            st.markdown(resposta.content)