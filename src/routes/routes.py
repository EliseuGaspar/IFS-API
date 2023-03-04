from flask import jsonify, redirect, request
from datetime import datetime

from ..app import app
from ..errors import error
from ..Models.YellowCards import yellowcard
from ..Models.Equipes import equipes
from ..Models.Partidas import partidas
from ..Models.RedCards import redcard
from ..Models.Gols import gols




@app.route('/', methods=['GET'])
def EndPoint():
	return jsonify(
		{'API':'API in Fly'}
	)

@app.route('/equipes', methods=['GET'])
def EndPointEquipes():
	return jsonify({"Response":equipes()})

@app.route('/info-clube/red-card/<string:name_team>/', methods=['GET'])
def EndPointInfoRedCard(name_team):
	return jsonify({f"{name_team}":redcard().Scraping(
			name_team,
			temporada
		)})

@app.route('/info-clube/yellow-card/<string:name_team>/', methods=['GET'])
def EndPointInfoYellowCard(name_team):
	return jsonify({f"{name_team}":yellowcard().Scraping(
			name_team,
			temporada
		)})

@app.route('/info-clube/gols/<string:name_team>/', methods=['GET'])
def EndPointInfoGols(name_team):
	return jsonify({f"{name_team}":gols().Scraping(
			name_team,
			temporada
		)})

@app.route('/info-clube/partidas/<string:name_team>/', methods=['GET'])
def EndPointInfoPartidas(name_team):
	return jsonify({f"{name_team}":partidas().Scraping(
			name_team,
			temporada
		)})

@app.route('/info-clube/<string:name_team>/',methods=['GET'])
def EndPointFullInfo(name_team):
	return jsonify()

@app.route('/info-clube/<string:name_team>/<string:str>',methods=['GET'])
def EndPointError(name_team, str):
	return jsonify({
		"response":"False endpoint"
		})