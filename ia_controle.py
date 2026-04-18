import os 
import time
import base64 #Transforma a imagem em um texto
import serial
from openai import OpenAI
from dotenv import load_dotenv
import cv2
from agno.tools.duckduckgo import DuckDuckGoTools

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

porta_serial = serial.Serial('COM4',9600)
time.sleep(2)

cap = cv2.VideoCapture(0)

print("Aperte F para a IA analisar sua imagem ou Q para sair")

while True:
    sucesso, frame = cap.read()
    
    cv2.imshow("Minha Câmera", frame)
    
    tecla = cv2.waitKey(1) #Espera um  milisegundo
    
    if tecla == ord('f'):
        print("🧠🤖 Aguarde que a IA está analisando a sua imagem...")
        _, buffer = cv2.imencode('.jpeg', frame)
        imagem_texto = base64.b64encode(buffer).decode('utf-8')
        
        resposta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role":"user",
                    "content":[
                        {
                            "type":"text", "text":"Existe um mosquetão nessa imagem, isso é fato. O mosquetão é um conector metálico de segurança com gatilho móvel, essencial em atividades verticais (escalada, rapel, resgate) e industriais para unir cordas ou equipamentos.A pergunta é: ele está corretamente e devidamente fechado? Responda com SIM ou NÃO"
                        },
                        {
                            "type": "image_url","image_url":{"url": f"data:image/jpeg;base64,{imagem_texto}"}
                        }
                    ]
       
                }
            ]
        )
        print("🤖 Resposta do CHAT GPT:")
        #Queremos somente  o conteúdo de resposta
        resultado = resposta.choices[0].message.content.upper()
        if "SIM" in resultado:
            print("Pessoa detectada! Ligando LED 🆗")
            porta_serial.write(b'1')
        else:
            print("Não detectado! Desligando LED ❌")
            porta_serial.write(b'0')
        
    elif tecla == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
porta_serial.close()
