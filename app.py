import json
import gradio as gr
from textblob import TextBlob
from googletrans import Translator

translator = Translator()

def sentiment_analysis(text: str) -> str:
    """
    Analiza el sentimiento de un texto en inglés o español.
    Si el texto no está en inglés, se traduce automáticamente antes de analizar.
    Devuelve polaridad, subjetividad y evaluación general.
    """
    if not text.strip():
        return json.dumps({"error": "Por favor ingresa un texto válido"}, ensure_ascii=False, indent=2)

    try:
        # Detectar idioma usando googletrans
        detection = translator.detect(text)
        lang = detection.lang
        confidence = detection.confidence

        # Traducir si no está en inglés
        if lang != "en":
            translated = translator.translate(text, src=lang, dest="en").text
        else:
            translated = text

        # Analizar sentimiento con TextBlob
        blob = TextBlob(translated)
        sentiment = blob.sentiment

        result = {
            "original_text": text,
            "detected_language": lang,
            "language_confidence": round(confidence, 2) if confidence else "N/A",
            "translated_text": translated if lang != "en" else "No translation needed",
            "polarity": round(sentiment.polarity, 2),
            "subjectivity": round(sentiment.subjectivity, 2),
            "assessment": (
                "positive" if sentiment.polarity > 0
                else "negative" if sentiment.polarity < 0
                else "neutral"
            )
        }

        return json.dumps(result, ensure_ascii=False, indent=2)

    except Exception as e:
        return json.dumps({
            "error": "Error al procesar el texto",
            "details": str(e)
        }, ensure_ascii=False, indent=2)

demo = gr.Interface(
    fn=sentiment_analysis,
    inputs=gr.Textbox(
        placeholder="Escribí texto en inglés o español...",
        lines=5,
        label="Texto a Analizar"
    ),
    outputs=gr.Textbox(
        lines=15,
        label="Resultado del Análisis",
        show_copy_button=True
    ),
    title="Multilingual Sentiment Analysis",
    description="Detecta idioma automáticamente, traduce y analiza sentimiento con TextBlob.",
    theme=gr.themes.Soft()
)

if __name__ == "__main__":
    demo.launch(mcp_server=True)
