# 🎙️ Voice-Based YouTube Song Searcher (en Español)

Este proyecto te permite realizar búsquedas de canciones en YouTube usando comandos de voz en español. Utiliza reconocimiento de voz con `SpeechRecognition`, extracción de videos con `yt_dlp` y abre automáticamente el resultado en tu navegador predeterminado.

---

## ✨ Características

- Reconocimiento de voz en español (`es-ES`)
- Busca canciones en YouTube usando solo tu voz
- Abre automáticamente el video más relevante en el navegador
- No descarga ningún contenido, solo muestra el enlace

---

## 🛠️ Requisitos

Asegúrate de tener instalado lo siguiente:

- Python 3.7 o superior
- Módulos de Python:
  - `speechrecognition`
  - `yt-dlp`
  - `pyaudio` (necesario para usar el micrófono)
- Un micrófono funcional
- Conexión a internet

---

## 📦 Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/tu-usuario/voice-youtube-search.git
cd voice-youtube-search
```

2. Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

Si no tienes `pyaudio`, instálalo manualmente (puede requerir dependencias del sistema):

```bash
pip install pipwin
pipwin install pyaudio
```

3. Ejecuta el script:

```bash
python buscador_voz_youtube.py
```

---

## 🎤 Uso

1. Ejecuta el script.
2. Espera el mensaje **"Di el comando:"**
3. Pronuncia:  
   ```plaintext
   Busca [nombre de la canción]
   ```
   Por ejemplo: **"Busca Bohemian Rhapsody Queen"**
4. El navegador abrirá el primer resultado de YouTube automáticamente.

---

## 🧠 Tecnologías usadas

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [webbrowser (built-in)](https://docs.python.org/3/library/webbrowser.html)

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

## 🚀 Autor

Desarrollado por Julián Hernández.  
¡Contribuciones y sugerencias son bienvenidas!
