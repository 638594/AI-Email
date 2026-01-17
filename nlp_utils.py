import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import RSLPStemmer



def preprocessador_texto(texto):
    if not texto:
        return ""
    
    # 1. Converter para minúsculas
    texto = texto.lower()
    
    # 2. Tokenização (dividir em palavras)
    tokens = word_tokenize(texto)
    
    # 3. Remover Pontuação e Stop Words 
    punctuation = set(string.punctuation)
    stop_words = set(stopwords.words('portuguese'))
    
    tokens = [t for t in tokens if t not in stop_words and t not in punctuation]
    
    # 4. Stemming (Reduzir ao radical)
    stemmer = RSLPStemmer()
    tokens_processadors = [stemmer.stem(t) for t in tokens]
    
    # Retorna o texto limpo como uma string única
    return " ".join(tokens_processadors)