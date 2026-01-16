from dotenv import load_dotenv
from flask import Flask, render_template, request
from nlp_utils import preprocessador_texto
from AI_analyzer import analisar_com_gemini
from textFIleExtractor import extrair_texto_arquivo

app = Flask(__name__)

load_dotenv()

@app.route('/', methods=['GET', 'POST'])
def index():
    texto_limpo = None
    texto_original = ""
    analise_ia = None
    
    if request.method == 'POST':
        
        if 'arquivo' in request.files and request.files['arquivo'].filename != '':
            arquivo = request.files['arquivo']
            texto_original = extrair_texto_arquivo(arquivo)
        else:
            
            texto_original = request.form.get('meu_texto')
            
        if texto_original:
            texto_limpo = preprocessador_texto(texto_original)
            analise_ia = analisar_com_gemini(texto_limpo)

    return render_template('index.html',
                           original=texto_original,
                           limpo =texto_limpo,
                           analise = analise_ia
                           )

if __name__ == '__main__':
    app.run(debug=True)