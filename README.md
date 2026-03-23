# Analizador de Sentimientos con NLP

He desarrollado este proyecto para explorar el mundo del Procesamiento de Lenguaje Natural (NLP). El objetivo es procesar cadenas de texto y determinar, mediante algoritmos de aprendizaje, si la connotación es positiva, negativa o neutra.

## ¿Por qué usé TextBlob?
Después de investigar varias opciones como NLTK o Spacy, elegí **TextBlob** para este proyecto inicial porque:
1. Ofrece una interfaz muy sencilla y limpia para tareas comunes de NLP.
2. Su propiedad `.sentiment.polarity` permite obtener un valor numérico exacto (de -1 a 1), lo que da mucha precisión si luego quisiera graficar los resultados.

## Lógica detrás del código
En lugar de crear un analizador basado en reglas manuales (lo cual sería imposible por la complejidad del lenguaje), decidí enfocarlo así:
1. **Modularización:** Creé una función dedicada `analizar_sentimiento` que separa la lógica del análisis del flujo principal del programa.
2. **Interpretación de Scores:** No me limité a mostrar un número; el código traduce la "polaridad" en etiquetas legibles (Positivo/Negativo) para que sea útil para un usuario final.
3. **Manejo de Idioma:** Aunque está optimizado para inglés (donde los modelos de TextBlob son más fuertes), la estructura está preparada para escalar a un sistema de traducción automática en el futuro.