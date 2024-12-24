### Ollama commands
```bash
ollama run llama3
ollama pull mistral
```

### Langchain documentation
Link to output_parsers [Output Parsers](https://python.langchain.com/v0.1/docs/modules/model_io/output_parsers/)


### Definitions, acronyms
Alucinación (Hallucination):

Definición: El modelo genera información incorrecta o completamente inventada sin que haya una base clara en los datos de entrada. Esto sucede cuando el modelo "alucina" hechos, detalles o respuestas que no son reales.
Ejemplo: El modelo responde con información falsa sobre una persona famosa o inventa una función de una biblioteca de software que no existe.

Example of Hallucination:
Prompt: "Who discovered the theory of relativity?"
Hallucinated Response: "The theory of relativity was discovered by Isaac Newton in 1905."
Issue: While the response seems confident and plausible, it is incorrect. The theory of relativity was actually developed by Albert Einstein, not Isaac Newton.


### (Operador Pipe | ): Line code "summary_prompt_template | llm | StrOutputParser()" 
tubería de procesamiento (pipeline) utilizando operadores de piping (|), 
que son comunes en ciertas librerías o frameworks para conectar diferentes operaciones de 
forma secuencial en Python. Aunque este operador no es nativo en Python y es introducido 
por algunas librerías (como transformers, langchain, o toolz)

| (Operador Pipe):

El operador | se usa para encadenar las operaciones. Básicamente, toma la salida de un objeto y la pasa como entrada al siguiente en la cadena.
En este caso, la entrada es procesada de la siguiente manera:
La plantilla (summary_prompt_template) se pasa al modelo de lenguaje (llm).
El resultado del modelo (llm) se pasa al parser de salida (StrOutputParser()).
Resumen de lo que hace la línea de código:
Esta línea parece construir una tubería de procesamiento donde:

Se pasa una plantilla (summary_prompt_template) como entrada.
La plantilla es procesada por un modelo de lenguaje (llm) que genera una salida basada en esa plantilla.
La salida del modelo es parseada por el StrOutputParser(), probablemente para formatearla o convertirla en una cadena de texto.
Visualización del flujo:
scss
Copy code
(summary_prompt_template) --> (llm) --> (StrOutputParser())

