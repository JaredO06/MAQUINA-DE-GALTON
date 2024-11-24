Pokedex

import requests
import os
import json

# Diccionario para asociar tipos de Pokémon con símbolos
TIPOS_EMOJIS = {
    "fire": "🔥",
    "water": "💧",
    "electric": "⚡",
    "grass": "🌿",
    "ice": "❄️",
    "fighting": "🥊",
    "poison": "☠️",
    "ground": "🌍",
    "flying": "🕊️",
    "psychic": "🔮",
    "bug": "🐛",
    "rock": "🪨",
    "ghost": "👻",
    "dragon": "🐉",
    "dark": "🌑",
    "steel": "⚙️",
    "fairy": "✨",
    "normal": "🔵"
}

# Función para buscar un Pokémon
def buscar_pokemon(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print("\n❌ Pokémon no encontrado. Intenta con otro nombre.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"\n⚠️ Error al conectar con la API: {e}")
        return None

# Función para mostrar datos en pantalla
def mostrar_datos(data):
    nombre = data["name"]
    peso = data["weight"]
    altura = data["height"]
    tipos = [f"{TIPOS_EMOJIS.get(tipo['type']['name'], '❔')} {tipo['type']['name']}" for tipo in data["types"]]
    habilidades = [habilidad["ability"]["name"] for habilidad in data["abilities"]]
    movimientos = [mov["move"]["name"] for mov in data["moves"][:5]]  # Limitar a 5 movimientos.

    print(f"\n✅ Nombre: {nombre.capitalize()}")
    print(f"⚖️  Peso: {peso}")
    print(f"📏 Altura: {altura}")
    print(f"🌀 Tipos: {', '.join(tipos)}")
    print(f"✨ Habilidades: {', '.join(habilidades)}")
    print(f"🌀 Movimientos: {', '.join(movimientos)}")

# Función para guardar datos en un archivo JSON
def guardar_pokemon(data):
    if not os.path.exists("pokedex"):
        os.makedirs("pokedex")
    
    nombre = data["name"]
    archivo = os.path.join("pokedex", f"{nombre}.json")
    
    with open(archivo, "w") as f:
        json.dump(data, f, indent=4)
    
    print(f"\n💾 Datos de {nombre.capitalize()} guardados en '{archivo}'")

# Programa principal
if __name__ == "__main__":
    print("¡Bienvenido a la Pokédex!")
    nombre_pokemon = input("Introduce el nombre de un Pokémon: ").strip()

    if not nombre_pokemon:
        print("\n⚠️ Debes introducir un nombre.")
    else:
        data = buscar_pokemon(nombre_pokemon)
        if data:
            mostrar_datos(data)
            guardar_pokemon(data)

