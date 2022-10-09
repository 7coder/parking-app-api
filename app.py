import json
import sqlite3
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from pathlib import Path

from db.init_db import init_db_exec
from db.connection import get_db_connection

class VueFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        variable_start_string='%%',
        variable_end_string='%%',
    ))

app = VueFlask(__name__,  static_folder = "./dist/static", template_folder = "./dist")
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/permits", methods=["GET", "POST"])
def permits():
    if request.method == "GET":
        conn = get_db_connection()
        permits = conn.execute("SELECT * FROM permits")

        if request.args.get('licensePlateNumber'):
            permits = conn.execute("SELECT * FROM permits\
                 WHERE licensePlateNumber = ?", (request.args.get('licensePlateNumber'), ))
        
        if request.args.get('ownerName'):
            permits = conn.execute("SELECT * FROM permits\
                 WHERE ownerName = ?",  (request.args.get('ownerName'), ))
                
        return jsonify([ dict(permit) for permit in permits.fetchall()])

    if request.method == "POST":
        req = request.get_json()
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO permits \
                (licensePlateNumber, plateIssuerCountry, startDate, endDate, ownerName )\
                    values (?, ?, ?, ?, ?)", 
                    [
                        req.get("licensePlateNumber"), 
                        req.get("plateIssuerCountry"),
                        req.get("startDate"), 
                        req.get("endDate"), 
                        req.get("ownerName")
                    ]
                    )
        conn.commit()
        return jsonify("ok")

if __name__ == '__main__':
    db = Path("./db/database.db")
    if not db.is_file():
        init_db_exec()

    app.run(debug=True)