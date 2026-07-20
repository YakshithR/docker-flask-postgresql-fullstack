from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os
import socket

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://13.51.249.6:8080"}})
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "demo")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")


def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


@app.route("/", methods=["GET"])
def home():

    hostname = socket.gethostname()

    try:
        pod_ip = socket.gethostbyname(hostname)
    except:
        pod_ip = "Unknown"

    return jsonify({
        "message": "Backend Running",
        "pod_name": hostname,
        "pod_ip": pod_ip
    })


@app.route("/users", methods=["POST"])
def add_user():

    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users(name) VALUES (%s)",
        (data["name"],)
    )

    conn.commit()

    cur.close()
    conn.close()

    return jsonify({
        "message": "User Saved Successfully"
    })


@app.route("/users", methods=["GET"])
def get_users():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM users ORDER BY id")

    users = cur.fetchall()

    cur.close()
    conn.close()

    result = []

    for user in users:
        result.append({
            "id": user[0],
            "name": user[1]
        })

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
