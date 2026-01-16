from PyPDF2 import PdfReader  

def extrair_texto_arquivo(arquivo):
    nome_arquivo = arquivo.filename.lower()
    conteudo = ""
    
    
    if nome_arquivo.endswith(".txt"):
        conteudo = arquivo.read().decode('utf-8')
        
    elif nome_arquivo.endswith(".pdf"):
        pdf_reader = PdfReader(arquivo)
        for pagina in pdf_reader.pages:
            conteudo += pagina.extract_text()
    
    return conteudo
