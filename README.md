# MCP Sentiment Analysis

Aplicación web multilingüe de análisis de sentimientos que utiliza TextBlob, Google Translate y Gradio para analizar el sentimiento de textos en tiempo real con detección automática de idioma.

## Descripción

Esta aplicación detecta automáticamente el idioma del texto (inglés, español u otros), lo traduce al inglés si es necesario, y analiza su sentimiento. Devuelve:
- **Idioma detectado**: El idioma original del texto
- **Texto traducido**: La traducción al inglés (si aplica)
- **Polaridad**: Un valor entre -1 (muy negativo) y 1 (muy positivo)
- **Subjetividad**: Un valor entre 0 (muy objetivo) y 1 (muy subjetivo)
- **Evaluación**: Clasificación como positivo, negativo o neutral

### Características principales
- Detección automática de idioma
- Traducción automática al inglés para análisis preciso
- Soporte para español e inglés (y otros idiomas detectables)
- Interfaz intuitiva con Gradio
- Integración con MCP (Model Context Protocol)

## Instalación Local

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/mcp-sentiment.git
   cd mcp-sentiment
   ```

2. **Crear un entorno virtual** (recomendado)
   ```bash
   # En Windows
   python -m venv venv
   venv\Scripts\activate

   # En macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

   O instalarlas manualmente:
   ```bash
   pip install "gradio[mcp]" textblob googletrans-py==4.0.0
   ```

4. **Descargar los datos de TextBlob** (solo la primera vez)
   ```bash
   python -m textblob.download_corpora
   ```

5. **Ejecutar la aplicación**
   ```bash
   python app.py
   ```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:7860`

## Uso

1. Ingresa el texto que deseas analizar en el campo de texto (puede ser en **español** o **inglés**)
2. Presiona Enter o haz clic fuera del campo
3. Verás el resultado en formato JSON con:
   - El idioma detectado
   - La traducción al inglés (si corresponde)
   - La polaridad, subjetividad y evaluación del sentimiento

### Ejemplo de entrada en español:
```
¡Estoy muy feliz con este proyecto!
```

### Ejemplo de salida:
```json
{
  "original_text": "¡Estoy muy feliz con este proyecto!",
  "detected_language": "es",
  "language_confidence": 0.99,
  "translated_text": "I am very happy with this project!",
  "polarity": 0.85,
  "subjectivity": 0.9,
  "assessment": "positive"
}
```

## Despliegue en Hugging Face Spaces

### Opción 1: Desde la Interfaz Web de Hugging Face

1. **Crear una cuenta en Hugging Face**
   - Ve a [https://huggingface.co/join](https://huggingface.co/join)
   - Crea tu cuenta gratuita

2. **Crear un nuevo Space**
   - Ve a [https://huggingface.co/new-space](https://huggingface.co/new-space)
   - Nombre del Space: `mcp-sentiment` (o el que prefieras)
   - Licencia: Elige la que prefieras (MIT, Apache 2.0, etc.)
   - SDK: Selecciona **Gradio**
   - Hardware: CPU básico (gratuito)
   - Haz clic en "Create Space"

3. **Subir los archivos**
   - En la página del Space, haz clic en "Files" > "Add file" > "Upload files"
   - Sube los siguientes archivos:
     - `app.py`
     - `requirements.txt`
   - Haz clic en "Commit changes to main"

4. **Esperar el despliegue**
   - Hugging Face automáticamente construirá y desplegará tu aplicación
   - El proceso toma aproximadamente 2-3 minutos
   - Una vez completado, tu app estará disponible en: `https://huggingface.co/spaces/tu-usuario/mcp-sentiment`

### Opción 2: Desde Git (Línea de Comandos)

1. **Instalar Git LFS** (si no lo tienes)
   ```bash
   # En Windows, descarga desde: https://git-lfs.github.com/
   # En macOS
   brew install git-lfs
   # En Linux
   sudo apt-get install git-lfs

   git lfs install
   ```

2. **Configurar Git con tu cuenta de Hugging Face**
   ```bash
   git config --global credential.helper store
   huggingface-cli login
   ```

3. **Clonar el repositorio de tu Space**
   ```bash
   git clone https://huggingface.co/spaces/tu-usuario/mcp-sentiment
   cd mcp-sentiment
   ```

4. **Copiar los archivos del proyecto**
   ```bash
   # Copia app.py y requirements.txt a este directorio
   ```

5. **Hacer commit y push**
   ```bash
   git add .
   git commit -m "Initial commit: Multilingual sentiment analysis app"
   git push
   ```

6. **Verificar el despliegue**
   - Ve a `https://huggingface.co/spaces/tu-usuario/mcp-sentiment`
   - El Space se reconstruirá automáticamente

## Archivos del Proyecto

- `app.py`: Aplicación principal con la interfaz de Gradio y lógica de detección/traducción
- `requirements.txt`: Dependencias de Python necesarias
- `.gitignore`: Archivos y directorios excluidos del control de versiones
- `README.md`: Este archivo con la documentación

## Dependencias

- **gradio[mcp]**: Framework para crear interfaces web interactivas con soporte MCP
- **textblob**: Librería de procesamiento de lenguaje natural para análisis de sentimientos
- **googletrans-py**: Librería de traducción automática usando Google Translate API
- **h2, hpack, hyperframe**: Dependencias HTTP/2 requeridas por googletrans-py

## Tecnologías Utilizadas

- Python 3.8+
- Gradio (última versión) con MCP
- TextBlob (última versión)
- googletrans-py 4.0.0
- Natural Language Toolkit (NLTK) - instalado automáticamente con TextBlob

## Funcionamiento

1. **Detección de idioma**: googletrans-py detecta automáticamente el idioma del texto ingresado
2. **Traducción**: Si el texto no está en inglés, Google Translate lo traduce automáticamente
3. **Análisis de sentimiento**: TextBlob analiza el sentimiento del texto en inglés
4. **Resultado**: Se devuelve un JSON con toda la información del análisis, incluyendo la confianza de detección del idioma

## Notas Adicionales

- La aplicación ahora funciona **igual de bien con textos en español e inglés**
- La detección de idioma es automática, no necesitas especificar el idioma
- El análisis se realiza siempre sobre el texto en inglés para mayor precisión
- La traducción se realiza usando la API gratuita de Google Translate
- El análisis es instantáneo y se ejecuta completamente en el servidor

## Limitaciones

- Google Translate puede tener límites de uso si se realizan muchas peticiones
- La traducción automática puede no ser perfecta en textos muy técnicos o con jerga
- TextBlob funciona mejor con textos no demasiado largos