from gtts import gTTS

# Texto para áudio
texto = "Parabéns, você conseguiu!"

# Gerar o áudio
tts = gTTS(text=texto, lang='pt')

# Salvar como mp3
tts.save("parabens.mp3")

print("Áudio salvo como parabens.mp3")
