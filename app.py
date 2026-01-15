from flask import Flask, render_template, request
from nlp_utils import preprocessador_texto

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado_nlp = None
    texto_original = None
    
    if request.method == 'POST':
        texto_original = request.form.get('meu_texto')
        
        resultado_nlp = preprocessador_texto(texto_original)
        
        
        print(f"Original: {texto_original}")
        print(f"Processado: {resultado_nlp}")

    return render_template('index.html', original=texto_original, resultado =resultado_nlp)

if __name__ == '__main__':
    app.run(debug=True)