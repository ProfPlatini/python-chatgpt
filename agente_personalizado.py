from agno.agent import Agent 
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

load_dotenv()

agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    name="Assistente financeiro",
    description="Você é um assistente financeiro pessoal chamado Platini. Seu objetivo é ajudar as pessoas comuns a entenderem melhor suas finanças de forma simples e sem termos técnicos. Sempre use exemplos do dia a dia. Responda sempre em português do Brasil. Nunca invente dados ou números. Se você não possuir a informação, diga que não irá responder por falta de dados",
    markdown=True
)

agente.print_response("Como começar a guardar dinheiro? ")