# Respuestas predefinidas
respuestas = [
    "Hola :)",
    "Estoy bien, ¿y tú?",
    "¿De qué te gustaría hablar?",
    "Es un tema interesante, pero no estoy preparado para esa conversación :(",
    "Si, me encanta la comida rápida :3",
    "Me alegra saberlo"
]

# Función para obtener la respuesta del programa
def obtener_respuesta(pregunta):
    if pregunta.lower() == "hola":
        return respuestas[0]
    elif "cómo estás" in pregunta.lower():
        return respuestas[1]
    elif "como estas" in pregunta.lower():
        return respuestas[1]
    elif "bien gracias" in pregunta.lower():
        return respuestas[5]
    elif "te gusta la comida rápida?" in pregunta.lower():
        return respuestas[4]
    elif "te gustan las hamburguesas" in pregunta.lower():
        return respuestas[4]
    else:
        return respuestas[3]

# Bucle principal
while True:
    pregunta = input("Usuario: ")
    respuesta = obtener_respuesta(pregunta)
    print("Programa:", respuesta)

    continuar = input("¿Quieres seguir conversando? (s/n): ")
    if continuar.lower() != "s":
        break
