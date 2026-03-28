from dotenv import load_dotenv 

load_dotenv()

chave = load_dotenv()

if chave:
    print("Chave carregada com sucesso ")
    print(chave)
else: 
    print("Chave não encontrada")