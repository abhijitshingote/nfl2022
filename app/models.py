from app import db

class Team(db.Model):
    team_id = db.Column(db.Integer, primary_key=True,autoincrement=False)
    team_location = db.Column(db.String, unique=False, nullable=False)
    team_name = db.Column(db.String, unique=True, nullable=False)
    logo_href = db.Column(db.String, unique=True, nullable=False)
    division = db.Column(db.String, unique=False, nullable=False)

class Game(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    game_id =db.Column(db.String, primary_key=False)
    season_type =db.Column(db.String, unique=False, nullable=False)
    game_number =db.Column(db.String, unique=False, nullable=False)
    game_name =db.Column(db.String, unique=False, nullable=False)
    game_date =db.Column(db.DateTime, unique=False, nullable=False)
    home_team_id =db.Column(db.Integer, primary_key=False)
    away_team_id =db.Column(db.Integer, primary_key=False)
    home_team_score =db.Column(db.Integer, primary_key=False)
    away_team_score=db.Column(db.Integer, primary_key=False)
    winner_team_id= db.Column(db.Integer, primary_key=False)


class TeamGame(db.Model):
    team_game_id =db.Column(db.Integer, primary_key=True)
    team_id =db.Column(db.Integer, unique=True, nullable=False)
    game_id =db.Column(db.String, unique=True, nullable=False)
    result =db.Column(db.String, unique=True, nullable=False)
    home_away =db.Column(db.String, unique=True, nullable=False)

class PassingStats(db.Model):
    passingstats_id = db.Column(db.Integer, primary_key=True)
    team_game_id = db.Column(db.String, unique=True, nullable=False)
    yards = db.Column(db.String, unique=True, nullable=False)
    drives = db.Column(db.String, unique=True, nullable=False)
    turnovers = db.Column(db.String, unique=True, nullable=False)
    passes = db.Column(db.String, unique=True, nullable=False)
    yardsperpass = db.Column(db.String, unique=True, nullable=False)

