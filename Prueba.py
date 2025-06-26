import json

def alternar_configuracion(ruta_json="configuracion.json"):
    def alternar(valor, opciones=None):
        if opciones:
            try:
                idx = opciones.index(valor)
                return opciones[(idx + 1) % len(opciones)]
            except ValueError:
                return opciones[0]
        return not valor

    # Cargar configuración
    with open(ruta_json, "r", encoding="utf-8") as archivo:
        config = json.load(archivo)

    # Alternar valores
    config["accesibilidad"] = alternar(config.get("accesibilidad", False))
    config["musica"] = alternar(config.get("musica", True))
    config["dificultad"] = alternar(config.get("dificultad", "facil"), ["facil", "medio", "dificil", "arcade"])

    # Guardar configuración modificada
    with open(ruta_json, "w", encoding="utf-8") as archivo:
        json.dump(config, archivo, indent=2, ensure_ascii=False)

    return config