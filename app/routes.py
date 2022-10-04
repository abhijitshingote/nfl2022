from app import application,db
from app.models import Team,Game
from flask import render_template
import requests

@application.route("/")
def hello_world():
    return "<p>Hello, Radhika World!!!!</p>"

@application.route("/index/")
def teams_():
    response=requests.get('https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/teams?limit=32').json()['items']
    teams=[]
    for r in response:
        team={}
        response=requests.get(r['$ref']).json()
        team['location']=response['location']
        team['name']=response['name']
        team['logo']=response['logos'][0]['href']
        teams.append(team)
    return render_template('index.html',teams=teams)

@app.route("/teams/")
def teams():
    teams=Team.query.all()
    return render_template('teams.html',teams=teams)

@app.route("/teams/<id>/")
def team_events(id):
    team=db.session.query(Team).filter(Team.team_id==id).all()[0]
    games=db.session.query(Game).filter((Game.home_team_id==id) | (Game.away_team_id==id) ).order_by(Game.game_date)
    return render_template('games.html',games=games,team=team)