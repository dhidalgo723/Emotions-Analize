from textblob import TextBlob

def analizar_sentimiento(texto):
    """
    Analiza la polaridad de un texto. 
    Polaridad > 0: Positivo
    Polaridad < 0: Negativo
    Polaridad == 0: Neutro
    """
    analisis = TextBlob(texto)
    # Traducimos si es necesario (opcional, TextBlob funciona mejor en ingles)
    # polaridad va de -1.0 a 1.0
    polaridad = analisis.sentiment.polarity
    
    if polaridad > 0:
        return "Positivo", polaridad
    elif polaridad < 0:
        return "Negativo", polaridad
    else:
        return "Neutro", polaridad

# Lista de frases para probar el script
frases = [
    "I love this new Python project, it is amazing!",
    "This is the worst bug I have ever seen in my life.",
    "The weather today is normal, nothing special.",
    "Programming in Java is challenging but very rewarding."
]

print("--- Resultados del Analizador de Sentimientos ---")
for frase in frases:
    resultado, score = analizar_sentimiento(frase)
    print(f"Frase: {frase}")
    print(f"Sentimiento: {resultado} (Score: {score})\n")