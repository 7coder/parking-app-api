import json
import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS
from pathlib import Path

from db.init_db import init_db_exec
from db.connection import get_db_connection


app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/permits", methods=["GET", "POST"])
def permits():
    if request.method == "GET":
        conn = get_db_connection()
        permits = conn.execute("SELECT * FROM permits")    
        return jsonify(list(permits))

    if request.method == "POST":
        return jsonify(request.get_json())
        


if __name__ == '__main__':
    db = Path("./db/database.db")
    if not db.is_file():
        init_db_exec()

    app.run(debug=True)