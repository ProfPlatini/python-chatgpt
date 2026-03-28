from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
import requests

# Carrega as variáveis de ambiente (sua chave da OpenAI no arquivo .env)
load_dotenv()

# ==========================================
# ⚠️ COLOQUE AQUI O IP QUE APARECEU NO MONITOR SERIAL DO ARDUINO
IP_DO_ESP32 = "192.168.15.6"  # <-- Lembre os alunos de mudarem isso!
# ==========================================

# A ferramenta enxuta e direta ao ponto
def controlar_maquina_fisica(comando: str) -> str: #O trecho comando: str) -> str: é o que chamamos de Type Hint (Dica de Tipo).
    
    """Liga ou desliga a máquina física. O comando deve ser 'ligar' ou 'desligar'."""
    
    # Faz a requisição direto para o ESP32 usando a palavra que a IA escolheu
    requests.get(f"http://{IP_DO_ESP32}/{comando}")
    
    # Avisa o "cérebro" da IA que a ação terminou
    return "Ação executada no hardware."

# Configurando o Agente
agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description="Você é um Agente de Controle Industrial. Seu trabalho é operar o hardware da fábrica quando o humano pedir.",
    tools=[controlar_maquina_fisica],  # Entregamos a ferramenta para a IA
    markdown=True
)

print("=" * 50)
print("🤖 AGENTE IoT OPERACIONAL E CONECTADO")
print("=" * 50)

# Loop infinito para conversar com o Agente
while True:
    mensagem = input("\nOperador: ")
    if mensagem.lower() == "sair":
        print("Desligando o sistema...")
        break
    else:
        # stream=True faz o texto aparecer digitando aos poucos (efeito legal na tela)
        agente.print_response(mensagem, stream=True)