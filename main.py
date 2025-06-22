import random

preguntas = [
    {
        "categoria": "Matemática",
        "dificultad": "Fácil",
        "pregunta": "¿Cuánto es 7 x 6?",
        "opciones": ["A) 42", "B) 36", "C) 48", "D) 30"],
        "respuesta": "A"
    },
    {
        "categoria": "Historia",
        "dificultad": "Media",
        "pregunta": "¿En qué año fue la Revolución de Mayo?",
        "opciones": ["A) 1816", "B) 1810", "C) 1820", "D) 1806"],
        "respuesta": "B"
    },
    {
        "categoria": "Lengua",
        "dificultad": "Fácil",
        "pregunta": "¿Cuál es el sustantivo en la oración: 'El perro corre rápido'?",
        "opciones": ["A) corre", "B) rápido", "C) perro", "D) El"],
        "respuesta": "C"
    },
    {
        "categoria": "Geografía",
        "dificultad": "Media",
        "pregunta": "¿Cuál es el país más grande del mundo?",
        "opciones": ["A) China", "B) Canadá", "C) Estados Unidos", "D) Rusia"],
        "respuesta": "D"
    },
    {
        "categoria": "Ciencias Naturales",
        "dificultad": "Difícil",
        "pregunta": "¿Cuál es el símbolo químico del oro?",
        "opciones": ["A) Ag", "B) Au", "C) Hg", "D) Fe"],
        "respuesta": "B"
    },
    {
        "categoria": "Educación Física",
        "dificultad": "Media",
        "pregunta": "¿Cuántos jugadores hay en un equipo de vóley?",
        "opciones": ["A) 6", "B) 5", "C) 7", "D) 11"],
        "respuesta": "A"
    },
    {
        "categoria": "Informática",
        "dificultad": "Difícil",
        "pregunta": "¿Qué significa 'CPU'?",
        "opciones": ["A) Central Process Unit", "B) Control Processing Unit", "C) Central Processing Unit", "D) Computer Primary Unit"],
        "respuesta": "C"
    }
]

# ----- Configuración de puntaje -----
valores_dificultad = {
    "Fácil": 10,
    "Media": 20,
    "Difícil": 30
}

# ----- Funciones -----

def mostrar_introduccion():
    print("🏫 Bienvenido al Colegio Embrujado")
    print("Los profesores fantasma quieren evaluarte una vez más...")
    print("Si respondés mal 5 veces, suena la alarma y ¡te expulsan!\n")

def mostrar_pregunta(pregunta, numero):
    print("---------------------------------------------")
    print("👻 Profesor de", pregunta["categoria"])
    print("Pregunta", numero)
    print("Dificultad:", pregunta["dificultad"])
    print(pregunta["pregunta"])
    for opcion in pregunta["opciones"]:
        print(opcion)

def obtener_puntaje(dificultad):
    return valores_dificultad.get(dificultad, 0)

def procesar_respuesta(respuesta_usuario, respuesta_correcta):
    return respuesta_usuario == respuesta_correcta

def mostrar_resultado_final(puntaje, sanciones, max_sanciones):
    print("\n📋 Resultado Final:")
    print("Puntaje total:", puntaje)
    print("Sanciones acumuladas:", sanciones)
    if sanciones < max_sanciones:
        print("🎉 ¡Lograste salir del colegio embrujado con vida!")
    else:
        print("💀 Fuiste expulsado. Mejor suerte la próxima...")

def jugar_trivia(preguntas, max_sanciones):
    puntaje = 0
    sanciones = 0
    numero_pregunta = 1

    random.shuffle(preguntas)

    for pregunta in preguntas:
        mostrar_pregunta(pregunta, numero_pregunta)
        respuesta = input("Elegí tu respuesta (A, B, C o D): ").upper()

        if procesar_respuesta(respuesta, pregunta["respuesta"]):
            puntos = obtener_puntaje(pregunta["dificultad"])
            puntaje += puntos
            print("✅ ¡Correcto! Sumás", puntos, "puntos.")
        else:
            sanciones += 1
            print("❌ Incorrecto. Llevás", sanciones, "sanciones.")
            if sanciones >= max_sanciones:
                print("🚨 ¡Sonó la alarma! Fuiste expulsado.")
                break

        numero_pregunta += 1

    mostrar_resultado_final(puntaje, sanciones, max_sanciones)

# ----- Ejecución -----

def main():
    mostrar_introduccion()
    jugar_trivia(preguntas, max_sanciones=5)

main()