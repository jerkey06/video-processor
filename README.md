# Video Processor

Video Processor es una aplicación Python que procesa automáticamente archivos de video para crear versiones editadas concisas eliminando contenido redundante. Utiliza detección de voz, transcripción y AI para identificar y remover segmentos duplicados mientras mantiene el contenido principal del video.

## 🚀 Características
- Detección automática de voz en videos
- Transcripción de audio usando múltiples proveedores de AI:
  - OpenAI (Whisper)
  - DeepSeek Audio
  - Google Gemini Pro
- Filtrado inteligente de contenido usando:
  - GPT-4
  - DeepSeek Chat
  - Gemini Pro
- Edición y compilación automática de video
- Soporte para múltiples formatos (.mp4, .mov, .avi, .mkv)

## 📁 Estructura del Proyecto
```
video_processor/
├── requirements.txt      # Dependencias del proyecto
├── .env                 # Variables de entorno
├── README.md           # Documentación
├── src/                # Código fuente
│   ├── main.py        # Punto de entrada
│   ├── config.py      # Configuración
│   ├── services/      # Servicios principales
│   │   ├── audio_service.py        # Procesamiento de audio
│   │   ├── transcription_service.py # Transcripción
│   │   ├── llm_service.py          # Filtrado AI
│   │   └── video_service.py        # Edición de video
│   └── utils/         # Funciones auxiliares
│       └── file_utils.py
├── raw/               # Videos de entrada
└── edited/            # Videos procesados
```

## 📋 Prerrequisitos
- Python 3.8 o superior
- FFmpeg instalado en el sistema
- API key de OpenAI, DeepSeek o Gemmini

## 🛠️ Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/jerkey06/video-processor.git
cd video-processor
```

2. Crea y activa un entorno virtual:
```bash
python -m venv venv

# En Windows:
venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Configuración de API:

### Opción 1: OpenAI API
1. Ve a [OpenAI's platform](https://platform.openai.com/account/api-keys)
2. Regístrate o inicia sesión
3. Ve a "API Keys" en la barra lateral
4. Haz clic en "Create new secret key"
5. Copia la clave generada

### Opción 2: DeepSeek API
1. Ve a [DeepSeek's platform](https://platform.deepseek.com/)
2. Crea una cuenta e inicia sesión
3. Ve a la sección "API Keys"
4. Genera una nueva API key

### Opción 3: Google Gemini API
1. Ve a [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Inicia sesión con tu cuenta de Google
3. Haz clic en "Get API key"
4. Crea una nueva API key o usa una existente

5. Crea un archivo `.env` en la raíz del proyecto y añade las keys que vayas a usar:
```
OPENAI_API_KEY=tu_api_key_aquí
DEEPSEEK_API_KEY=tu_api_key_aquí
GEMINI_API_KEY=tu_api_key_aquí
```

## 💻 Uso

1. Configura el proveedor de AI que deseas usar en `src/config.py`:
```python
class Config:
    AI_PROVIDER = "openai"  # Opciones: "openai", "deepseek", "gemini"
```

2. Coloca tus archivos de video en el directorio `raw/`

3. Ejecuta el procesador:
```bash
python src/main.py
```

4. Encuentra los videos procesados en el directorio `edited/`

## 💰 Comparación de Precios de API

### OpenAI
- Whisper API: $0.006 / minuto
- GPT-4: Desde $0.03 / 1K tokens

### DeepSeek
- Transcripción de Audio: $0.004 / minuto
- Modelo de Chat: Desde $0.001 / 1K tokens

### Google Gemini
- Gemini Pro: $0.00025 / 1K tokens (¡Gratis hasta cierto uso!)
- Audio Processing: Incluido en el precio base

*Nota: Los precios pueden variar. Consulta las páginas oficiales para las tarifas actuales:*
- [OpenAI Pricing](https://openai.com/pricing)
- [DeepSeek Pricing](https://platform.deepseek.com/pricing)
- [Google AI Pricing](https://ai.google.dev/pricing)

## ⚠️ Solución de Problemas

### FFmpeg no encontrado
- Asegúrate de que FFmpeg esté instalado y accesible en el PATH del sistema
- Windows: Descarga e instala desde ffmpeg.org
- macOS: `brew install ffmpeg`
- Linux: `sudo apt-get install ffmpeg`

### Errores de API OpenAI
- "Insufficient quota": Verifica tus límites de uso y estado de facturación
- "Rate limit reached": Espera unos minutos o aumenta tus límites
- "Invalid API key": Revisa tu API key en el archivo .env

### Errores de API DeepSeek
- "Authentication failed": Verifica que tu API key esté correctamente copiada
- "Quota exceeded": Revisa tu saldo en DeepSeek
- "Model not available": Asegúrate de usar los nombres correctos de modelos

### Errores de API Gemini
- "API key not valid": Verifica que tu API key de Google esté activa
- "Quota exceeded": Revisa tus límites de uso gratuito
- "Region not supported": Asegúrate que el servicio esté disponible en tu región

### Problemas de Memoria
- Intenta procesar segmentos de video más cortos
- Asegura suficiente memoria del sistema
- Cierra otras aplicaciones que consuman mucha memoria

## 🤝 Contribuir

Para contribuir al proyecto:

1. Haz fork del repositorio
2. Crea una rama para tu feature
3. Realiza tus cambios
4. Envía un pull request

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para detalles.

## 🌟 Reconocimientos

Este proyecto utiliza varias librerías y APIs de código abierto:
- OpenAI Whisper y GPT
- DeepSeek Audio y Chat
- WebRTC VAD
- MoviePy
- pydub
- LangChain

