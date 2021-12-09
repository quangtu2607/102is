from operator import length_hint
from re import match
from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
import pickle
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

@app.route("/match", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        pass
    else:
        matches = []
        for u in Match.query.all():
            temp = u.__dict__
            del temp['_sa_instance_state']
            matches.append(temp)
        response = jsonify(matches)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route("/predict", methods=['POST'])
def predict():
    import numpy as np
    with open('./static/model/randomforest.pkl', 'rb') as f:
        load_model = pickle.load(f)
    match_stats = request.json
    datapoint = np.array([[match_stats['FTHG'], match_stats['FTAG'], match_stats['HS'], match_stats['AS'],\
                           match_stats['HST'], match_stats['AST'], match_stats['HF'], match_stats['AF'],\
                           match_stats['HC'], match_stats['AC'], match_stats['HY'], \
                           match_stats['AY'], match_stats['HR'], match_stats['AR']]])
    result = load_model.predict_proba(datapoint).flatten()
    response = {'A': result[0], 'D': result[1], 'H': result[2]}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, port=80)
