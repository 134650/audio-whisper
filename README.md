
# 🎧 audio-whisper

Este projeto permite **transcrever áudios** e **gerar um resumo dos pontos-chave** automaticamente. A transcrição é feita utilizando o modelo **Whisper (OpenAI)** e a sumarização é realizada através do modelo **Llama 3** rodando localmente via **Ollama**.

---

## 🚀 Funcionalidades

- 🎙️ Transcrição automática de áudios em português ou outros idiomas.
- ✍️ Geração de resumos com os principais pontos da fala.
- 🔥 Funciona offline após instalação dos modelos (Whisper + Ollama).

---

## 🛠️ Instalação

### 1️⃣ Clone este repositório:

```bash
git clone https://github.com/seu-usuario/audio-whisper.git
cd audio-whisper
```

### 2️⃣ Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3️⃣ Instale as dependências:

```bash
pip install -r requirements.txt
```

**Exemplo de `requirements.txt`:**

```
openai-whisper
requests
```

### 4️⃣ Instale e configure o Ollama (para sumarização):

- Baixe e instale via: https://ollama.com
- Inicie o Ollama no terminal:

```bash
ollama serve
```

- Baixe um modelo, por exemplo:

```bash
ollama pull llama3
```

---

## 📁 Estrutura do projeto

```
audio-whisper/
├── audio/                         # Pasta para arquivos de áudio
├── gerar-audio/                    # Scripts para gerar áudios (opcional)
│   └── gerar-audio.py
├── transcribe_and_summarize.py     # Script principal de transcrição e resumo
├── requirements.txt
└── README.md
```

---

## ▶️ Como executar

1️⃣ Coloque seus arquivos de áudio na pasta `audio/`.

2️⃣ Execute o script:

```bash
python transcribe_and_summarize.py
```

Por padrão, o script está configurado para processar o arquivo `audio/parabens.mp3`. Você pode alterar o caminho no arquivo `transcribe_and_summarize.py` na variável:

```python
caminho_audio = r"C:\Users\seu-usuario\audio-whisper\audio\parabens.mp3"
```

---

## 💡 Exemplo de uso

### 🔊 Arquivo de entrada:

`audio/parabens.mp3` contendo uma frase.

### 🖥️ Saída no terminal:

```
[1] Transcrevendo áudio...
Transcrição completa.

[2] Extraindo pontos-chave com Ollama...

Resumo dos Pontos-Chave:

- Parabéns, você conseguiu!
```

---

## 📝 Observações

- Modelos maiores do Whisper como `medium` ou `large` geram transcrições mais precisas.
- O Ollama precisa estar rodando localmente para o resumo funcionar.
- O projeto é totalmente offline após baixar os modelos.
