# poke-api - _A little  pokemon-API_

Esta API desarrollada en Flask permite gestionar una base de datos de Pokémon haciendo uso de SQLite. Puedes realizar las siguientes acciones:

* Obtener un mensaje de bienvenida.
* Listar todos los Pokémon.
* Insertar un nuevo Pokémon.
* Eliminar un Pokémon por su ID.

## Requisitos
* Python 3.x
* Flask
* SQLite
## Instalación
1. Clona este repositorio o descarga los archivos.
2. Instala las dependencias ejecutando el siguiente comando en tu terminal:

```bash
pip install flask
```
3. Crea la base de datos SQLite y la tabla pokemon si aún no existe. En dado caso has uso del archivo ```dump.sql``` y algún software cliente de SQL, recomiendo [DBeaver](https://dbeaver.io/download/).

4. Guarda la base de datos en una carpeta llamada ```database``` con el nombre pokedb en el directorio raíz del proyecto.

## Ejecución
Navega al directorio donde se encuentra tu archivo de la API (app.py).

Ejecuta el servidor con el siguiente comando:

```bash
python -m flask run
```
Si todo está configurado correctamente, el servidor se ejecutará en http://127.0.0.1:5000/.

## Endpoints
```GET /``` 

Retorna un mensaje de bienvenida.

Respuesta Exitosa (200):
```json
{
    "message": "Hola Mundo Python!"
}
```

```GET /getAllPokemon```

Devuelve una lista de todos los Pokémon en la base de datos.

Respuesta Exitosa (200): Un array con los Pokémon.
```json
[
    {
        "id": 1,
        "name": "Bulbasaur",
        "type_primary": "Grass",
        "type_secondary": "Poison"
    },
    ...
]
```

```POST /insertPokemon```

Inserta un nuevo Pokémon en la base de datos.

Datos del cuerpo de la solicitud (JSON):

```json
{
    "name": "Pikachu",
    "type_primary": "Electric",
    "type_secondary": null
}
```
Respuesta Exitosa (201):

```json
{
    "message": "Pokémon insertado con éxito"
}
```
Respuesta de Error (400):

```json
{
    "error": "Faltan campos requeridos"
}
```

```DELETE /deletePokemon/<id>```

Elimina un Pokémon de la base de datos según su ID.

Respuesta Exitosa (200):

```json
{
    "message": "Pokémon eliminado con éxito"
}
```

Respuesta de Error (404):

```json
{
    "error": "Pokémon no encontrado"
}
```

## Notas
* Asegúrate de que la base de datos esté correctamente configurada en la carpeta database/pokedb.
* Puedes modificar la estructura de la tabla o agregar más funcionalidades según sea necesario.
