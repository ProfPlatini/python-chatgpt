# Importa a biblioteca OpenCV, responsável por ligar a câmera e lidar com imagens
import cv2 

# Importa a biblioteca base64, que serve para transformar arquivos (como imagens) em textos longos
import base64 

# Importa a biblioteca os (Sistema Operacional), usada para ler variáveis do seu computador (como senhas)
import os 

# Importa a ferramenta principal da OpenAI para conseguirmos falar com o ChatGPT
from openai import OpenAI 

# Importa a função que lê o arquivo .env (onde guardamos senhas e chaves secretas com segurança)
from dotenv import load_dotenv 

# Carrega as configurações ocultas do arquivo .env para a memória do programa
load_dotenv() 

# Cria o "cliente" da OpenAI, entregando a nossa chave de acesso para ele saber quem está pagando a conta
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) 

# -----------------------------------------------------------------------------

# Liga a câmera. O número 0 indica que queremos usar a primeira câmera conectada (padrão do notebook)
cap = cv2.VideoCapture(0) 

# Imprime na tela preta (terminal) as instruções para o usuário saber o que fazer
print("Aperte 'A' para a IA analisar a cena, ou 'Q' para sair.") 

# Cria um loop infinito. O vídeo nada mais é do que várias fotos passando muito rápido sem parar
while True:
    
    # Tira a "foto" daquele exato milissegundo. 'sucesso' diz se deu certo, 'frame' é a imagem em si
    sucesso, frame = cap.read() 
    
    # Abre uma janelinha no computador chamada "Olho da Inteligencia Artificial" e mostra a imagem (frame) nela
    cv2.imshow("Olho da Inteligencia Artificial", frame) 
    
    # O programa pausa por 1 milissegundo e verifica se o usuário apertou alguma tecla
    tecla = cv2.waitKey(1) & 0xFF 
    
    # Se a tecla apertada for 'a' (minúsculo)...
    if tecla == ord('a'): 
        # Avisa o usuário que o processo começou
        print("\n🧠 Enviando a imagem para o cérebro da IA... Aguarde!") 
        
        # 1. O TRUQUE: O ChatGPT não tem "olhos" para ver um arquivo de imagem normal. 
        # Pegamos a imagem atual (frame) e codificamos ela num formato de arquivo temporário '.jpg'
        _, buffer = cv2.imencode('.jpg', frame) 
        
        # Transformamos essa imagem temporária num texto gigante (Base64) que a IA consegue ler
        imagem_texto = base64.b64encode(buffer).decode('utf-8') 
        
        # 2. Fazemos o pedido oficial para a API da OpenAI (modelo gpt-4o-mini, que entende visão)
        resposta = client.chat.completions.create(
            model="gpt-4o-mini", # Escolhe o modelo rápido e barato
            messages=[ # Lista de mensagens da conversa
                {
                    "role": "user", # Indica que é o usuário (nós) falando
                    "content": [
                        # Passamos o texto com o comando (prompt)
                        {"type": "text", "text": "Descreva o que você está vendo de forma muito bem humorada e sarcástica."},
                        # Passamos a imagem convertida naquele texto gigante
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{imagem_texto}"}}
                    ]
                }
            ]
        )
        
        # 3. Quando a IA responde, mostramos um aviso no terminal
        print("🤖 ChatGPT diz:") 
        # Navegamos pela resposta da OpenAI até pegar apenas o texto final que ela gerou e imprimimos
        print(resposta.choices[0].message.content) 
        
    # Se a tecla apertada não for 'a', mas for 'q' (minúsculo)...
    elif tecla == ord('q'): 
        # Quebra o loop infinito, o que faz o programa parar de rodar
        break 

# -----------------------------------------------------------------------------

# Desliga a câmera corretamente para ela não ficar com a luzinha acesa roubando bateria
cap.release() 

# Fecha todas as janelinhas de vídeo que o OpenCV abriu no computador
cv2.destroyAllWindows()