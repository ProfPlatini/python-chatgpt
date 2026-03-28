from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()

banco = SqliteDb(db_file="tmp/busca.db")

agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description="Você é um assistente de pesquisa. Responda em português.",
    db=banco,
    add_history_to_context=True,
    num_history_runs=3,
    tools=[DuckDuckGoTools()],  # adicionando a ferramenta de busca
    markdown=True
)

print("-" * 30)
print("Bem-vindo ao agente de IA")
print("-" * 30)

while True:
    mensagem = input("Digite a sua pergunta:")
    if mensagem.lower() == "sair":
        print("Finalizando agente...")
        break
    else:
        agente.print_response(mensagem, strem=True)