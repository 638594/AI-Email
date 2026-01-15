import os
import google.generativeai as genai
from dotenv import load_dotenv
from flask import Flask, render_template, request
from nlp_utils import preprocessador_texto
from google.generativeai.types import HarmCategory,HarmBlockThreshold

app = Flask(__name__)

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-3-flash-preview')

def analisar_com_gemini(texto_limpo):
    # Configuração para ignorar bloqueios de segurança bobos durante o teste
    safety_settings = {
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    }

    model = genai.GenerativeModel('gemini-3-flash-preview')
    
    prompt = f"""
    Com base nos radicais de palavras abaixo, siga estas regras:
    1. Classifique como 'Produtivo' ou 'Improdutivo'.
    2. Não dê justificativas.
    3. Escreva uma 'Sugestão de Resposta' curta e profissional.

    Texto processado: {texto_limpo}

    Formato de resposta desejado:
    Classificação: [Sua classificação]
    Sugestão: [Sua sugestão]
    """
    
    try:
        # Passamos as configurações de segurança aqui
        response = model.generate_content(
            prompt,
            safety_settings=safety_settings
        )
        
        # Verificamos se a resposta tem conteúdo antes de acessar .text
        if response.candidates and response.candidates[0].content.parts:
            return response.text
        else:
            return "A IA não conseguiu gerar uma resposta para este texto (bloqueio de segurança)."
            
    except Exception as e:
        return f"Erro: {str(e)}"
        

@app.route('/', methods=['GET', 'POST'])
def index():
    texto_limpo = None
    texto_original = None
    analise_ia = None
    
    if request.method == 'POST':
        texto_original = request.form.get('meu_texto')
        
        if texto_original:
        
            texto_limpo = preprocessador_texto(texto_original)
            
            analise_ia= analisar_com_gemini(texto_limpo)
        
        
        # print(f"Original: {texto_original}")
        # print(f"Processado: {resultado_nlp}")

    return render_template('index.html',
                           original=texto_original,
                           limpo =texto_limpo,
                           analise = analise_ia
                           )

if __name__ == '__main__':
    app.run(debug=True)