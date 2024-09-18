from flask import Flask, json, request
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("database/pokedb")
    conn.row_factory = sqlite3.Row  # Facilita conversión a JSON
    return conn


@app.route('/')
def getHolaMundo():
    return json.dumps({"message": 'Hola Mundo Python!'}), 200


# En este caso no se necesita de la declaración del método GET, por defecto Flask lo asume.
@app.route('/getAllPokemon')
def getAllPokemon():
    conn = get_db_connection()

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pokemon;")
    rows = cursor.fetchall()

    conn.close()

    res = json.dumps([dict(row) for row in rows])
    return res


@app.route('/insertPokemon', methods=['POST'])
def insertPokemon():
    data = request.get_json()  # Obtener los datos del cuerpo de la solicitud
    name = data.get('name')
    type_primary = data.get('type_primary')
    type_secondary = data.get('type_secondary')

    if not name or not type_primary:
        return json.dumps({"error": "Faltan campos requeridos"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('''INSERT INTO pokemon (name, type_primary, type_secondary)
                          VALUES (?, ?, ?)''', (name, type_primary, type_secondary))
        conn.commit()
        conn.close()
        return json.dumps({"message": "Pokémon insertado con éxito"}), 201
    except sqlite3.Error as e:
        conn.close()
        return json.dumps({"error": str(e)}), 500


@app.route('/deletePokemon/<int:id>', methods=['DELETE'])
def deletePokemon(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('DELETE FROM pokemon WHERE id = ?', (id,))
        conn.commit()

        if cursor.rowcount == 0:
            conn.close()
            return json.dumps({"error": "Pokémon no encontrado"}), 404

        conn.close()
        return json.dumps({"message": "Pokémon eliminado con éxito"}), 200
    except sqlite3.Error as e:
        conn.close()
        return json.dumps({"error": str(e)}), 500
