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

### Objetivo

Subir `mcp-sentiment` a Hugging Face Spaces para que cualquiera pueda conectarse al servidor vía:

```
https://TU-USUARIO-mcp-sentiment.hf.space/gradio_api/mcp/
```

---

### Paso 1 — Crear tu Space

1. Entrá a [ghttps://huggingface.co/spaces](https://huggingface.co/spaces)

2. Clic en **"New Space"**

3. Completá los siguientes datos:
   - **Name**: `mcp-bilingual-sentiment`
   - **Visibility**: `Public` (o Private)
   - **SDK**: `Gradio`
   - **Hardware**: `CPU Basic` (gratis)

4. Clic en **"Create Space"**

Listo! Te va a crear un repositorio del tipo:
```
https://huggingface.co/spaces/tu_usuario/mcp-sentiment
```

---

### Paso 2 — Preparar tu proyecto local

En tu carpeta `C:\Programming\mcp-sentiment`, asegurate de tener estos archivos:

```
mcp-sentiment/
├── app.py
└── requirements.txt
```

**Verificá que tu `requirements.txt` tenga:**

```txt
gradio[mcp]
textblob
googletrans-py==4.0.0
h2==4.3.0
hpack==4.1.0
hyperframe==6.1.0
```

⚠️ **Importante**: Hugging Face Spaces instala automáticamente las dependencias de este archivo.

---

### Paso 3 — Subir el código a Hugging Face

#### Opción A: Desde Git (Recomendado)

Desde tu terminal (asegurate de tener Git instalado):

```bash
cd C:\Programming\mcp-sentiment

# Agregar archivos importantes
git add app.py requirements.txt README.md .gitignore

# Hacer commit
git commit -m "Initial Hugging Face deployment"

# Configurar rama principal
git branch -M main

# Agregar remote de Hugging Face
git remote add space https://huggingface.co/spaces/TU_USUARIO/mcp-bilingual-sentiment

# Subir a Hugging Face
git push -u space main
```

**Primera vez usando Hugging Face?**
- Te va a pedir loguearte
- Usá tu **Access Token** que podés crear desde 👉 [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
- Cuando te pida username, poné tu nombre de usuario de HF
- Cuando te pida password, pegá el token (no tu contraseña)

#### Opción B: Desde la Interfaz Web

1. Entrá a tu Space recién creado
2. Clic en **"Files"** → **"Add file"** → **"Upload files"**
3. Arrastrá o seleccioná:
   - `app.py`
   - `requirements.txt`
4. Clic en **"Commit changes to main"**

---

### Paso 4 — Esperar a que se construya el Space

1. Entrá a tu Space: `https://huggingface.co/spaces/tu_usuario/mcp-sentiment`

2. Vas a ver que dice: **"Building app…"** (tarda 2-5 minutos)

3. Cuando termine, se abrirá la interfaz web de Gradio con tu app online

4. **Probá la app online**:
   - Ingresá un texto en español: `"Me encanta este proyecto"`
   - Debería devolver el análisis completo

---

### Paso 5 — Verificar el endpoint MCP

Tu Space ahora tiene un **endpoint MCP público** en:

```
https://tu_usuario-mcp-sentiment.hf.space/gradio_api/mcp/
```

Podés usar este endpoint desde:
- **Cursor IDE** con MCP
- **Claude Desktop** con MCP
- Cualquier cliente MCP remoto

#### Conectar desde Cursor IDE (Windows)

1. Abrí **Settings** → **Features** → **Model Context Protocol**

2. Editá tu archivo de configuración MCP y agregá:

```json
{
  "mcpServers": {
    "sentiment-analysis": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "@modelcontextprotocol/server-remote",
        "https://tu_usuario-mcp-sentiment.hf.space/gradio_api/mcp/",
        "--transport",
        "sse"
      ]
    }
  }
}
```

3. Reiniciá el IDE

4. Ahora podés usar el servidor MCP de sentiment analysis directamente desde tu IDE!

#### Conectar desde Claude Desktop

Editá el archivo de configuración de Claude Desktop:

**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

Agregá:

```json
{
  "mcpServers": {
    "sentiment-analysis": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-remote",
        "https://tu_usuario-mcp-sentiment.hf.space/gradio_api/mcp/"
      ]
    }
  }
}
```
---

### 🔧 Troubleshooting

**Problema: El Space no construye**
- Verificá que `requirements.txt` esté bien escrito
- Revisá los logs en la pestaña "Logs" del Space

**Problema: Error de traducción**
- `googletrans-py` a veces tiene límites de rate
- Considerá agregar reintentos o usar una API de traducción más robusta

**Problema: El endpoint MCP no responde**
- Asegurate que el Space esté en estado "Running" (verde)
- Verificá que la URL termine en `/gradio_api/mcp/`
- Intentá acceder primero a la UI web para "despertar" el Space

**Problema: No puedo hacer git push**
- Instalá Git LFS: `git lfs install`
- Creá un Access Token en Hugging Face
- Usá el token como password al hacer push

---

### Recursos Adicionales

- [Documentación de Gradio](https://www.gradio.app/docs)
- [Documentación de Hugging Face Spaces](https://huggingface.co/docs/hub/spaces)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
- [Gradio MCP Integration](https://www.gradio.app/guides/gradio-and-mcp)

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