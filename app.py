from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    resultado = None
    valor_original = None
    
    if request.method == 'POST':
        try:
            # Recebe o valor numérico enviado pelo formulário HTML
            valor_original = float(request.form.get('valor', 0))
            # Realiza um cálculo simples no Back-end (ex: conversão de Metros para Centímetros)
            resultado = valor_original * 100
        except ValueError:
            resultado = "Por favor, insira um número válido."

    return render_template('index.html', valor=valor_original, resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
