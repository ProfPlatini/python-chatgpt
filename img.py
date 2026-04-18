import os
import webbrowser #Biblioteca nativa 
from openai import OpenAI #Biblioteca OPENAI
from dotenv import load_dotenv #Biblioteca DOTENV para ler o env 

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("Bem-vindo ao gerador de Imagens 🖌️")

ideia = input("Descreva a imagem que gostaria de criar: ")

print("Gerando imagem ...")
print("\t🧑‍🎨🎨")

resposta = client.images.generate(
    model="dall-e-3",
    prompt=ideia,
    size="1024x1024", 
    moderation="standard",   
 # quality="standard",#Usando o DALL-E-3, apenas Standard e HD
    n=1,
)

url_imagem = resposta.data[0].url

print("Imagem gerada com sucesso! 🆗🤖")

webbrowser.open(url_imagem)