from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
import os

load_dotenv()

#Crio um banco de dados local 
banco = SqliteDb(db_file="tmp/historico.db")

agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description="Você é um assistente simpático. Responda em português.",
    db=banco,
    add_history_to_context=True,
    num_history_runs=3,
    markdown=True
)


agente.print_response(
    "O que você sabe sobre mim?",
    stream = True,
    session_id = "c4c86ff9-5c77-40ef-a5ee-51581f6d8082" #Pego esse Session Id no Data Base criado.
)
