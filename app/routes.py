from app import app,db
from app.models import Team,Game
from flask import render_template
import requests

from datetime import datetime
import pytz

@app.context_processor
def inject_now():
    def convert_dt_to_est(datetimeobj):
        return datetimeobj.astimezone(pytz.timezone('US/Eastern')).strftime('%Y-%b-%d----%A %I:%M %p')
    return {'now': datetime.utcnow(),
            'pytz':pytz,
            'convert_dt_to_est':convert_dt_to_est}

# @app.route("/")
# def hello_world():
#     return """<p><a href="{{url_for('teams')}}">All Teams</a></p>"""

@app.route("/")
def teams_():
    response=requests.get('https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events').json()
    week=response['$meta']['parameters']['week'][0]
    print(f'Week:{week}')
    games=db.session.query(Game).filter(Game.season_type=='2').filter((Game.game_number==week)).order_by(Game.game_date)
    # games=response
    print(games)
    return render_template('index.html',games=games)

@app.route("/teams/")
def teams():
    teams={}
    for division in ['NFC South','NFC North','AFC North','AFC South','AFC East','AFC West','NFC West','NFC East']:
        teams[division]=Team.query.filter(Team.division==division)
    return render_template('teams.html',teams=teams)

@app.route("/teams/<id>/")
def team_events(id):
    team=db.session.query(Team).filter(Team.team_id==id).all()[0]
    games=db.session.query(Game).filter(Game.season_type=='2').filter((Game.home_team_id==id) | (Game.away_team_id==id) ).order_by(Game.game_date)
    return render_template('games.html',games=games,team=team)