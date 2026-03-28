from agno.agent import Agent 
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from datetime import datetime # 1. Importamos o módulo de data

load_dotenv()

# 2. Pegamos a data atual do seu computador
hoje = datetime.now().strftime("%d/%m/%Y")

agente = Agent (
    model=OpenAIChat(id="gpt-5.4-mini"),
    # 3. Injetamos a variável 'hoje' usando o 'f' antes das aspas
    description=f"Você é um assistente simpático que responde em português. Para sua referência, hoje é dia {hoje}.",
    markdown=True,
)

# Agora ele vai acertar!
agente.print_response("Olá! Me diga, que dia é hoje e me conte uma curiosidade sobre esse dia!")