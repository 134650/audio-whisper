import whisper
import requests
import os

# CONFIGS
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3"  # ou outro modelo instalado

PASTA_AUDIO = os.path.join(os.getcwd(), "audio")

def transcrever_audio(caminho_audio):
    model = whisper.load_model("base")  # ou "small", "medium", "large"
    print(f"Transcrevendo: {os.path.basename(caminho_audio)}")
    resultado = model.transcribe(caminho_audio)
    return resultado["text"]

def extrair_pontos_chave(texto_transcrito):
    prompt = (
        "A seguir está uma transcrição de áudio. Extraia os principais pontos-chave "
        "de forma clara e concisa:\n\n" + texto_transcrito
    )

    resposta = requests.post(OLLAMA_URL, json={
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    })

    if resposta.status_code == 200:
        return resposta.json()["response"]
    else:
        raise Exception("Erro ao se comunicar com o Ollama")

def main():
    if not os.path.exists(PASTA_AUDIO):
        print(f"ERRO: Pasta não encontrada: {PASTA_AUDIO}")
        return

    arquivos_audio = [
        os.path.join(PASTA_AUDIO, f)
        for f in os.listdir(PASTA_AUDIO)
        if f.lower().endswith((".mp3", ".wav", ".m4a"))
    ]

    if not arquivos_audio:
        print("Aviso: Nenhum arquivo de audio encontrado na pasta 'audio/'.")
        return

    for arquivo in arquivos_audio:
        try:
            print("\n==============================")
            texto = transcrever_audio(arquivo)
            print("Transcrição concluída.")

            print("Extraindo pontos-chave com Ollama...")
            resumo = extrair_pontos_chave(texto)

            nome_base = os.path.splitext(os.path.basename(arquivo))[0]
            caminho_resumo = os.path.join(PASTA_AUDIO, f"{nome_base}_resumo.txt")

            with open(caminho_resumo, "w", encoding="utf-8") as f:
                f.write(resumo)

            print(f"Resumo salvo em: {caminho_resumo}")
            print("==============================\n")

        except Exception as e:
            print(f"Erro ao processar {arquivo}: {e}")

if __name__ == "__main__":
    main()
