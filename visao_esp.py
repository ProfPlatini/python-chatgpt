import cv2
import base64
import os
import serial  # Biblioteca para falar com o ESP32
import time
from openai import OpenAI
from dotenv import load_dotenv

# 1. CONFIGURAÇÕES INICIAIS
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# CONEXÃO COM ESP32: 
# IMPORTANTE: Mude 'COM3' para a porta que aparece no seu Arduino IDE!
# No Mac/Linux costuma ser algo como '/dev/ttyUSB0'
porta_serial = serial.Serial('COM5', 9600) 
time.sleep(2) # Espera o ESP32 reiniciar após conectar

cap = cv2.VideoCapture(0)

print("--- SISTEMA DE VISÃO IA ATIVO ---")
print("Aperte 'A' para analisar ou 'Q' para sair.")

while True:
    sucesso, frame = cap.read()
    cv2.imshow("Olho da IA - Professor Platini", frame)
    
    tecla = cv2.waitKey(1) & 0xFF
    
    if tecla == ord('a'):
        print("\n🧐 Analisando cena...")
        
        # Converte a imagem para Base64 (texto)
        _, buffer = cv2.imencode('.jpg', frame)
        imagem_texto = base64.b64encode(buffer).decode('utf-8')
        
        # 2. O PROMPT ESTRATÉGICO
        # Pedimos para a IA responder apenas SIM ou NAO para facilitar a lógica
        resposta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Existe uma garrafa de água nesta imagem? Responda apenas com a palavra 'SIM' ou 'NAO'."},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{imagem_texto}"}}
                    ]
                }
            ]
        )
        
        resultado = resposta.choices[0].message.content.upper()
        print(f"🤖 Resultado da IA: {resultado}")

        # 3. ENVIANDO COMANDO PARA O HARDWARE
        if "SIM" in resultado:
            print("✅ Garrafa detectada! Ligando Pino 19...")
            porta_serial.write(b'1') # Envia o byte '1' para o ESP32
        else:
            print("❌ Nada detectado. Desligando Pino 19...")
            porta_serial.write(b'0') # Envia o byte '0' para o ESP32
            
    elif tecla == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
porta_serial.close() # Fecha a conexão com o ESP32