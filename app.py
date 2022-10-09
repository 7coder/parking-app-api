import json
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/permits", methods=["GET", "POST"])
def permits():
    if request.method == "GET":
        permits = [
            {
                "licensePlateNumber": "M M 1",
                "plateIssuerCountry": "DE",
                "startDate": "2022-12-12",
                "endDate": "2022-12-13",
                "ownerName": "Max Mustermann"
            },
            {
                "licensePlateNumber": "AA-123-AA",
                "plateIssuerCountry": "FR",
                "startDate": "2022-12-12",
                "endDate": "2022-12-13",
                "ownerName": "Jean Dupont"
            },
            {
                "licensePlateNumber": "SD 12345",
                "plateIssuerCountry": "CH",
                "startDate": "2022-12-12",
                "endDate": "2022-12-13",
                "ownerName": "Erika Mustermann"
            },
            {
                "licensePlateNumber": "AT 123",
                "plateIssuerCountry": "AT",
                "startDate": "2022-12-12",
                "endDate": "2022-12-13",
                "ownerName": "Krethi Musterfrau"
            }
        ]
        return jsonify(permits)

    if request.method == "POST":
        return jsonify(request.get_json())
        


if __name__ == '__main__':
    app.run(debug=True)