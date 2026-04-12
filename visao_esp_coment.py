# ==============================================================================
# IMPORTAÇÕES: TRAZENDO OS "SUPERPODERES" PARA O PYTHON
# ==============================================================================

# pip install opencv-python openai python-dotenv pyserial

import cv2          # OpenCV: Os "olhos" do nosso programa. Cuida da webcam.
import base64       # Base64: O "tradutor" que transforma fotos em textos gigantes.
import os           # OS (Operating System): Permite ler variáveis do sistema (como senhas).
import serial       # PySerial: O "sistema nervoso", envia dados pelo cabo USB para o ESP32.
import time         # Time: O "relógio", usado para criar pausas e não afobar o código.
from openai import OpenAI      # OpenAI: O "cérebro" da Inteligência Artificial.
from dotenv import load_dotenv # DotEnv: O "cofre" que carrega nossa chave secreta com segurança.

# ==============================================================================
# PASSO 1: CONFIGURAÇÕES INICIAIS E CONEXÕES
# ==============================================================================

# Abre o "cofre" (arquivo .env) e carrega as senhas para a memória do computador
load_dotenv()

# Cria a conexão com a OpenAI apresentando o nosso "crachá" (a API Key)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# CONEXÃO COM O MUNDO FÍSICO (ESP32):
# Abre um "tubo de comunicação" na porta COM5 na velocidade de 9600 bits por segundo.
porta_serial = serial.Serial('COM5', 9600) 

# Pausa o programa por 2 segundos. Isso é crucial porque, ao conectar a porta serial,
# o ESP32 costuma reiniciar. Damos esse tempo para ele "acordar" antes de mandar comandos.
time.sleep(2) 

# Pega a chave da primeira câmera conectada ao computador (a câmera padrão)
cap = cv2.VideoCapture(0)

print("--- SISTEMA DE VISÃO IA ATIVO ---")
print("Aperte 'A' para analisar ou 'Q' para sair.")

# ==============================================================================
# PASSO 2: O LOOP PRINCIPAL (A VIDA DO PROGRAMA)
# ==============================================================================

# O loop infinito que mantém a câmera tirando fotos milissegundo a milissegundo
while True:
    
    # Tira a foto exata do momento. 'sucesso' diz se funcionou, 'frame' é a imagem.
    sucesso, frame = cap.read()
    
    # Mostra a imagem em uma janela para podermos ver o que o robô está vendo
    cv2.imshow("Olho da IA - Professor Platini", frame)
    
    # O programa "escuta" o teclado por 1 milissegundo para ver se alguém apertou algo
    tecla = cv2.waitKey(1) & 0xFF
    
    # Se a tecla apertada foi a letra 'a' minúscula, começa a mágica:
    if tecla == ord('a'):
        print("\n🧐 Analisando cena...")
        
        # PREPARAÇÃO DA IMAGEM:
        # A IA não lê arquivos normais pela API, então codificamos o 'frame' para '.jpg' na memória.
        _, buffer = cv2.imencode('.jpg', frame)
        
        # Transformamos a sopa de bits do '.jpg' em um texto gigante legível pela internet (Base64)
        imagem_texto = base64.b64encode(buffer).decode('utf-8')
        
        # ======================================================================
        # PASSO 3: O PEDIDO PARA A INTELIGÊNCIA ARTIFICIAL
        # ======================================================================
        
        # Enviamos uma mensagem para o modelo gpt-4o-mini
        resposta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        # O "Prompt Estratégico": Limitamos a IA a falar apenas SIM ou NAO.
                        # Isso impede que ela conte uma história e quebre a lógica do IF abaixo.
                        {"type": "text", "text": "Existe uma garrafa de água nesta imagem? Responda apenas com a palavra 'SIM' ou 'NAO'."},
                        
                        # Anexamos a imagem em formato de texto Base64
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{imagem_texto}"}}
                    ]
                }
            ]
        )
        
        # Pegamos a resposta final da IA, e o '.upper()' garante que o texto fique em MAIÚSCULAS 
        # (evitando erros caso ela responda "Sim" ou "sim")
        resultado = resposta.choices[0].message.content.upper()
        print(f"🤖 Resultado da IA: {resultado}")

        # ======================================================================
        # PASSO 4: DECISÃO E COMANDO PARA O HARDWARE (ESP32)
        # ======================================================================
        
        # Se a palavra "SIM" estiver dentro da resposta da IA...
        if "SIM" in resultado:
            print("✅ Garrafa detectada! Ligando Pino 19...")
            
            # Escrevemos a letra '1' (em formato de byte, por isso o 'b') no cabo USB
            porta_serial.write(b'1') 
            
        # Caso contrário (se ela disser NAO)...
        else:
            print("❌ Nada detectado. Desligando Pino 19...")
            
            # Escrevemos a letra '0' (em formato de byte) no cabo USB
            porta_serial.write(b'0') 
            
    # Se a tecla apertada foi a letra 'q' minúscula...
    elif tecla == ord('q'):
        # Quebra o loop infinito, o que nos leva para as linhas de encerramento
        break

# ==============================================================================
# PASSO 5: LIMPEZA E ENCERRAMENTO (BOAS PRÁTICAS)
# ==============================================================================

# "Devolve" a câmera para o computador (apaga a luzinha da webcam)
cap.release()

# Fecha a janela do OpenCV ("Olho da IA")
cv2.destroyAllWindows()

# Desconecta o cabo USB eletronicamente, liberando a COM5 para outros programas
porta_serial.close()