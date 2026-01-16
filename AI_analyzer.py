import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def analisar_com_gemini(texto_limpo):
    

    model = genai.GenerativeModel('gemini-3-flash-preview')
    
    prompt = f"""
    Com base nos radicais de palavras abaixo, siga estas regras:
    
    1. Classifique como 'Produtivo' ou 'Improdutivo'.
    Produtivo: Emails que requerem uma ação ou resposta específica 
    (ex.: solicitações de suporte técnico, atualização sobre casos em aberto, 
    dúvidas sobre o sistema).
    Improdutivo: Emails que não necessitam de uma ação imediata
    (ex.: mensagens de felicitações, agradecimentos).
    2. Não dê justificativas.
    3. Escreva uma 'Sugestão de Resposta' curta e profissional.

    Texto processado: {texto_limpo}

    Formato de resposta desejado:
    Classificação: [Sua classificação]
    Sugestão: [Sua sugestão]
    """
    
    try:
        
        response = model.generate_content(
            prompt
           
        )
        
        # Verificamos se a resposta tem conteúdo antes de acessar .text
        if response.candidates and response.candidates[0].content.parts:
            return response.text
        else:
            return "A IA não conseguiu gerar uma resposta para este texto (bloqueio de segurança)."
            
    except Exception as e:
        return f"Erro: {str(e)}"

