import os 
import base64 #Transforma a imagem em um texto
from openai import OpenAI
from dotenv import load_dotenv
import cv2

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
                            "type":"text", "text":"Descreva o que vê de forma irônica"
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
        print(resposta.choices[0].message.content)
        
    elif tecla == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
