# ==========================================
# PASSO 1: IMPORTANDO AS FERRAMENTAS (A nossa caixa de ferramentas)
# Professor fala: "Primeiro, vamos chamar todo mundo que vai trabalhar no nosso projeto hoje."
# ==========================================
import streamlit as st                  # O nosso Front-end mágico (desenha a tela web).
from agno.agent import Agent            # O "Cérebro" do nosso assistente.
from agno.db.sqlite import SqliteDb     # O nosso Banco de Dados (para a IA ter memória).
from agno.models.openai import OpenAIChat # A conexão com o modelo do ChatGPT.
from agno.tools.duckduckgo import DuckDuckGoTools # A ferramenta que dá acesso à internet para a IA.
from dotenv import load_dotenv          # O cofre que guarda nossa chave secreta da API.

# Professor fala: "Agora, mandamos o Python abrir o cofre e ler a nossa chave da OpenAI."
load_dotenv()

# ==========================================
# PASSO 2: DESENHANDO A TELA (A Vitrine)
# Professor fala: "Vamos criar a cara do nosso site usando apenas duas linhas de código!"
# ==========================================
st.title("🔎 Assistente de Pesquisa com IA") # Cria um título grande e bonito no topo do site.
st.write("Faça uma pergunta e eu vou buscar na internet para você!") # Um texto menor de subtítulo.

# ==========================================
# PASSO 3: CONFIGURANDO A IA (O Back-end)
# Professor fala: "O Streamlit tem amnésia e recarrega a página toda hora. 
# Para ele não criar um banco de dados novo a cada clique, usamos esse 'cache'."
# ==========================================
@st.cache_resource
def iniciar_agente():
    # Cria o arquivo de banco de dados na pasta 'tmp' chamado 'busca.db'
    banco = SqliteDb(db_file="tmp/busca.db")
    
    # Configura todas as regras da nossa IA
    return Agent(
        model=OpenAIChat(id="gpt-4o-mini"), # Escolhemos o modelo mais rápido e barato
        description="Você é um assistente de pesquisa. Responda em português.", # A personalidade dela
        db=banco, # Ligamos a IA ao banco de dados que criamos acima
        add_history_to_context=True, # Ligamos a memória dela (para lembrar do que falamos)
        num_history_runs=3, # Ela vai lembrar das últimas 3 interações
        tools=[DuckDuckGoTools()], # Entregamos o 'celular com internet' para ela pesquisar
        markdown=True # Permite que ela use negrito, listas e tabelas nas respostas
    )

# Aqui nós executamos a função acima e guardamos o agente pronto na variável 'agente'
agente = iniciar_agente()

# ==========================================
# PASSO 4: CRIANDO O CHAT (A Interação)
# Professor fala: "Adeus 'input()' do terminal! Vamos criar uma caixa de texto de site de verdade."
# ==========================================
# Essa linha cria a caixinha de texto lá embaixo. O que o aluno digitar fica salvo em 'mensagem'.
mensagem = st.chat_input("Digite a sua pergunta:")

# Só entra nesse bloco IF se o usuário tiver digitado alguma coisa e apertado Enter
if mensagem:
    
    # 4.1: Mostrando a pergunta do usuário na tela
    with st.chat_message("user"): # Cria um balãozinho de chat com o ícone de usuário
        st.write(mensagem)        # Escreve dentro do balão o que a pessoa digitou

    # 4.2: Fazendo a IA responder
    with st.chat_message("assistant"): # Cria um balãozinho de chat com o ícone de robô
        
        # Cria aquele efeito visual legal de "carregando..." enquanto a IA pesquisa
        with st.spinner("Pesquisando na internet..."):
            
            # Aqui é o coração do código: Mandamos a pergunta para a IA e guardamos a 'resposta'
            # Detalhe: Usamos .run() em vez de .print_response() porque não queremos imprimir no terminal escuro!
            resposta = agente.run(mensagem)
            
            # Finalmente, pegamos o conteúdo da resposta e desenhamos na tela do site
            st.write(resposta.content)