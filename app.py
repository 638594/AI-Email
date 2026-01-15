from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    texto_recebido = None
    
    if request.method == 'POST':
        # 'meu_texto' é o atributo 'name' do input no HTML
        texto_recebido = request.form.get('meu_texto')
        print(f"Texto capturado: {texto_recebido}")
        # Aqui você pode salvar no banco, processar com IA, etc.

    return render_template('index.html', texto=texto_recebido)

if __name__ == '__main__':
    app.run(debug=True)