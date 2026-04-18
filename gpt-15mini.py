from openai import OpenAI
import base64
import os
import webbrowser #Biblioteca nativa 
from openai import OpenAI #Biblioteca OPENAI
from dotenv import load_dotenv #Biblioteca DOTENV para ler o env 

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

ideia = input("Descreva a sua imagem: ")

result = client.images.generate(
    model="gpt-image-1-mini",
    prompt=ideia,
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("otter.png", "wb") as f:
    f.write(image_bytes)