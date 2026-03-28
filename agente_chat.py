# agente_chat.py
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

load_dotenv()

banco = SqliteDb(db_file="tmp/chat.db")

agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description="Você é um assistente simpático. Responda em português.",
    db=banco,
    add_history_to_context=True,
    num_history_runs=10,
    markdown=True,
)


print("Agente iniciado! Digite 'sair' para encerrar.")

while True:

    mensagem = input("\nDigite a sua mensagem: ")

    if mensagem.lower() == "sair":
        print("Até mais!")
        break
    else:
        agente.print_response(mensagem, stream=True)