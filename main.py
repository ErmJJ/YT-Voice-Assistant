import speech_recognition as sr
import yt_dlp
import webbrowser

# Inicializar el reconocedor de voz
recognizer = sr.Recognizer()

# Escuchar el comando de voz
with sr.Microphone() as source:
    print("Di el comando:")
    audio = recognizer.listen(source)

    # Reconocer el comando de voz en español
    try:
        command = recognizer.recognize_google(audio, language='es-ES')
        print(f"Comando recibido: {command}")

        # Verificar si el comando comienza con "Busca"
        if command.lower().startswith('busca'):
            search_query = command[6:]  # Extraer la parte del comando después de "busca"

            # Buscar la canción en YouTube
            ydl_opts = {
                'format': 'bestaudio',
                'noplaylist': True,
                'quiet': True,
                'default_search': 'ytsearch1:',
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(search_query, download=False)
                video_url = info_dict['entries'][0]['webpage_url']

                # Abrir el navegador con la URL del video
                webbrowser.open(video_url)
        else:
            print("Comando no reconocido. Asegúrate de comenzar con 'Busca'.")

    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
    except sr.RequestError as e:
        print(f"Error de solicitud; {e}")
