POKEDEX

Pokédex en Python

Introducción

Este proyecto es una Pokédex creada en Python que utiliza la librería requests para conectarse a la API de Pokémon ( PokeAPI ). Como estudiante, el objetivo fue aprender a trabajar con solicitudes HTTP, manejar datos en formato JSON, interactuar con APIs y practicar el manejo de archivos.

La Pokédex permite al usuario buscar un Pokémon por nombre, mostrar su información (incluyendo emojis representativos de sus tipos) y guardar sus datos en un archivo JSON.

Características

Búsqueda de Pokémon: Conectándose a PokeAPI, el programa obtiene información sobre el Pokémon introducido.

Información detallada: Muestra el nombre, peso, altura, tipos (con emojis), habilidades y movimientos.

Emojis representativos: Cada tipo de Pokémon se muestra con un emoji relacionado (por ejemplo, 🔥 fire, ⚡ electric, etc.).

Almacenamiento en JSON: Los datos del Pokémon se guardan en un archivo JSON dentro de una carpeta llamada pokedex.

Validación de errores: Maneja errores en caso de que el Pokémon no exista o haya problemas de conexión con la API.

Tecnologías Utilizadas

Python

Librería Requests: Para realizar solicitudes HTTP.

Módulo OS: Para manejar rutas y crear carpetas.

Módulo JSON: Para manejar datos en formato JSON.

Estructura del Código

 Diccionario de Emojis

Se utilizó un diccionario llamado TIPOS_EMOJIS para mapear cada tipo de Pokémon a un emoji representativo

 Conexión con la API

Se usó la librería requests para conectarse a la API de Pokémon y obtener los datos
Mostrar Información

La función mostrar_datos toma los datos obtenidos de la API y los formatea para mostrarlos en la consola. Incluye los emojis según el tipo de Pokémon
Guardar en JSON

El programa crea una carpeta pokedex si no existe y guarda los datos del Pokémon en un archivo JSON
 Manejo de Errores

Se incluyen mensajes en caso de que el Pokémon no exista o haya un error de conexión
Lecciones Aprendidas

Solicitudes HTTP:

Aprendí a realizar solicitudes a APIs con requests y a manejar posibles errores de conexión.

Manejo de JSON:

Comprendí cómo trabajar con datos en formato JSON, extrayendo información relevante y guardándola en archivos.

Modularidad:

Dividí el programa en funciones para facilitar su organización y legibilidad.

Uso de Emojis:

Implementé un diccionario para asociar datos (tipos de Pokémon) con elementos visuales (emojis).

Validación y Manejo de Errores:

Aprendí la importancia de manejar casos excepcionales, como nombres de Pokémon inexistentes o fallos de red.

Conclusión

Este proyecto me permitió reforzar conocimientos en Python, especialmente en el uso de APIs y manejo de datos. Además, me enseñó a integrar elementos visuales simples, como emojis, para mejorar la experiencia del usuario. Es un punto de partida excelente para futuros proyectos más complejos relacionados con el desarrollo de aplicaciones y manejo de datos
