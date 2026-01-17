# 📧 AI Email Analyzer

Aplicação web simples desenvolvida com **Flask + IA (Google Gemini)** para classificar emails e sugerir respostas automáticas.

---

## 🚀 Funcionalidades

- Classificação de emails como **Produtivo** ou **Improdutivo**
- Geração de **sugestão de resposta automática**
- Entrada de texto manual ou upload de arquivos `.txt` e `.pdf`
- Interface web simples e organizada
- Integração com IA generativa (Gemini)

---

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- Flask
- Google Generative AI (Gemini)
- NLTK
- PyPDF2
- HTML + CSS

---

## 📁 Estrutura do Projeto

```
email-ia-classifier/
│
├── app.py
├── AI_analyzer.py
├── nlp_utils.py
├── textFIleExtractor.py
├── requirements.txt
├── .env
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## ⚙️ Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- **Python 3.10 ou superior**
- **pip**

---

## 🔑 Configuração da API do Gemini

1. Crie um arquivo chamado **`.env`** na raiz do projeto
2. Adicione sua chave da API do Gemini:

```env
GEMINI_API_KEY=SUA_CHAVE_AQUI
```


---

## ▶️ Como executar a aplicação localmente

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/638594/AI-Email.git
cd AI-Email
```

---

### 2️⃣ Criar ambiente virtual

```bash
python -m venv .venv
```

**Ativar o ambiente virtual:**

**Linux / macOS**
```bash
source .venv/bin/activate
```

**Windows**
```bash
.venv\Scripts\activate
```

---

### 3️⃣ Instalar as dependências

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Executar a aplicação

```bash
python app.py
```

---

### 5️⃣ Acessar no navegador

Abra o navegador e acesse:

```
http://127.0.0.1:5000
```

---

## 🧪 Como usar a aplicação

1. Cole o texto de um email **ou**
2. Envie um arquivo `.txt` ou `.pdf`
3. Clique em **Processar**
4. Visualize:
   - A **classificação do email**
   - A **sugestão de resposta gerada pela IA**

---

## ⚠️ Observações Importantes

- O NLTK faz download de recursos na **primeira execução**
- É necessário estar conectado à internet
- A resposta da IA depende das políticas do Google Gemini

---


## 👨‍💻 Autor

Desenvolvido por **Luiz Roberto Barreto Lima**  
Estudante de Ciência da Computação

---
