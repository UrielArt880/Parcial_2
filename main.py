import random
import re

def cargar_preguntas():
    lista_preguntas = []
    with open("preguntas.csv", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        lineas = lineas[1:]  # Saltear la primera línea (encabezados)

        for linea in lineas:
            elemento = re.split(",|\n", linea)  # Quita \n y separa por coma

            pregunta = {
                "categoria": elemento[0],
                "dificultad": elemento[1],
                "pregunta": elemento[2],
                "opciones": [
                    f"A) {elemento[3]}",
                    f"B) {elemento[4]}",
                    f"C) {elemento[5]}",
                    f"D) {elemento[6]}"
                ],
                "respuesta": elemento[7].upper(),
                "puntaje": elemento[8]
            }

            lista_preguntas.append(pregunta)

    return lista_preguntas

preguntas = cargar_preguntas()

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

def procesar_respuesta(respuesta_usuario, respuesta_correcta):
    correcto = False
    if respuesta_usuario == respuesta_correcta:
        correcto = True
    return correcto

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
    max_preguntas = 10
    
    random.shuffle(preguntas)

    for pregunta in preguntas:
        if numero_pregunta > max_preguntas:
            break
        
        mostrar_pregunta(pregunta, numero_pregunta)
        respuesta = input("Elegí tu respuesta (A, B, C o D): ")

        if procesar_respuesta(respuesta, pregunta["respuesta"]):
            puntos = int(pregunta["puntaje"])
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