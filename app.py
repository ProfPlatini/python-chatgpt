from flask import Flask

app = Flask (__name__)

@app.route("/")
def home():
    return "📚 Bem vindo ao site de livros do Platini 📚"

@app.route("/livroDoDia")
def livros():
    return "📚 O Castelo - Franz Kafka 📚"


if __name__ == '__main__':
    app.run("0.0.0.0",port=80)