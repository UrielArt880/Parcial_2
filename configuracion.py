
import re
import json
with open("preguntas.csv", "r") as archivo:
    for linea in archivo:
        registro = re.split(",|/n", linea)
        print(f"{registro[0]} - {registro[1]} - {registro[2]} - {registro[3]} - {registro[4]} - {registro[5]}\n")

with open("configuracion.json", "r") as archivo:
    config = json.load(archivo)

#Se activa Neurotipico para activar el modo Neurodivergente.

config["accesibilidad"] = not config["accesibilidad"]

config["musica"] = not config["musica"]

dificultades = ["facil", "medio", "dificil", "arcade"]
indice = dificultades.index(config["dificultad"])
config["dificultad"] = dificultades[(indice + 1) % len(dificultades)]

with open("configuracion.json", "w") as archivo:
    json.dump(config, archivo, indent=2, ensure_ascii=False)

print("Configuracion actualizada")