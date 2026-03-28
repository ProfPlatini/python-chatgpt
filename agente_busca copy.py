from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv


load_dotenv()

agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description="Você é um assistente de pesquisa. Responda em português.",
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
        agente.print_response(mensagem, stream=True)