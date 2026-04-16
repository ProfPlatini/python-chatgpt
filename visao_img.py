# ==============================================================================
# LENDO UMA IMAGEM DO COMPUTADOR E ENVIANDO PARA O CHATGPT
# ==============================================================================

# Importa o base64 para transformar o arquivo de imagem num texto gigante
import base64 

# Importa o os (Sistema Operacional) para ler a chave de segurança
import os 

# Importa a ferramenta do ChatGPT
from openai import OpenAI 

# Importa a biblioteca que lê o arquivo oculto .env
from dotenv import load_dotenv 

# Carrega as senhas do .env para a memória
load_dotenv() 

# Prepara o "carteiro" (client) da OpenAI com a nossa chave de acesso
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) 

# -----------------------------------------------------------------------------
# PASSO 1: ABRIR A IMAGEM DO COMPUTADOR
# -----------------------------------------------------------------------------

# Nome do arquivo que queremos ler. (Alerte os alunos: a foto precisa 
# estar na mesma pasta onde esse código Python está rodando!)
caminho_da_imagem = "foto.png"

print(f"Buscando a imagem '{caminho_da_imagem}' na pasta...")

# O comando 'with open' abre o arquivo. 
# O "rb" significa 'Read Binary' (Ler em Binário). O Python vai olhar para a foto
# não como uma imagem bonitinha, mas como uma sopa de números 0 e 1.
with open(caminho_da_imagem, "rb") as arquivo_imagem:
    
    # Lê os dados binários da imagem e já converte para o formato Base64 (texto)
    imagem_texto = base64.b64encode(arquivo_imagem.read()).decode('utf-8')

print("Imagem convertida com sucesso! Enviando para o cérebro da IA...\n")

# -----------------------------------------------------------------------------
# PASSO 2: ENVIAR PARA A INTELIGÊNCIA ARTIFICIAL
# -----------------------------------------------------------------------------

# Fazemos o pedido oficial para a API da OpenAI (modelo gpt-4o-mini)
resposta = client.chat.completions.create(
    model="gpt-4o-mini", 
    messages=[ 
        {
            "role": "user", 
            "content": [
                # Mandamos a instrução em formato de texto
                {"type": "text", "text": "Haja como um detetive e descreva todos os detalhes escondidos nessa imagem."},
                # Mandamos a nossa imagem que foi transformada em texto Base64
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{imagem_texto}"}}
            ]
        }
    ]
)

# -----------------------------------------------------------------------------
# PASSO 3: MOSTRAR A RESPOSTA
# -----------------------------------------------------------------------------

print("🕵️ Detetive IA diz:") 
print(resposta.choices[0].message.content)