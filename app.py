from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Aplicação Web de Teste</h1><p>Seu back-end em Python e Flask está funcionando online!</p>"

if __name__ == '__main__':
    app.run(debug=True)
