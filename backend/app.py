from operator import length_hint
from re import match
from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_h = db.Column(db.String(50), nullable=False)
    team_a = db.Column(db.String(50), nullable=False)
    finished = db.Column(db.Boolean, nullable=False)
    started = db.Column(db.Boolean, nullable=False)
    time = db.Column(db.DateTime, nullable=False)

def clean(raw_match, teams):
    raw_match['team_h'] = teams[raw_match['team_h'] - 1]['name']
    raw_match['team_a'] = teams[raw_match['team_a'] - 1]['name']
    raw_match['kickoff_time'] = datetime.datetime.strptime(raw_match['kickoff_time'],"%Y-%m-%dT%H:%M:%SZ")
    raw_match['rate'] = 'test'
    return raw_match

@app.route("/match", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        pass
    else:
        response = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/')
        teams = response.json()['teams']

        response = requests.get("https://fantasy.premierleague.com/api/fixtures/?future=1")
        raw_matches = response.json()
        matches = list(map(lambda x: clean(x, teams), raw_matches))
        matches = []
        for u in Match.query.all():
            temp = u.__dict__
            del temp['_sa_instance_state']
            matches.append(temp)
        response = jsonify(matches)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route("/predict/<int:id>", methods=['POST', 'GET'])
def predict(id):
    if request.method == 'POST':
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=80)
