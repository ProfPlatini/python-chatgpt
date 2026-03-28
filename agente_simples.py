from agno.agent import Agent 
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

load_dotenv()

agente = Agent (
    model=OpenAIChat(id="gpt-4o-mini"),
    description="Você é um assistente simpático que responde em português",
    markdown=True,
)

agente.print_response("Olá! Me conte uma curiosidade! ")