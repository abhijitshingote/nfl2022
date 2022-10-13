import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import time

user='postgres'
password='password'
host='postgres'
db='maindb'
engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:5432/{db}')
# engine = create_engine(f'postgresql+psycopg2://abhijit:masterradhika@awseb-e-ygd4gbhqep-stack-awsebrdsdatabase-rhau64iyrzj3.cvecty0kpthu.us-east-1.rds.amazonaws.com:5432/ebdb')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Team(Base):
    __tablename__="team"
    team_id = Column(Integer, primary_key=True,autoincrement=False)
    team_location = Column(String, unique=False, nullable=False)
    team_name = Column(String, unique=True, nullable=False)
    logo_href = Column(String, unique=True, nullable=False)
    division = Column(String, unique=False, nullable=False) 
    
class Game(Base):
    __tablename__="game"
    id = Column(Integer,primary_key=True,autoincrement=True)
    game_id = Column(String, primary_key=False)
    season_type = Column(String, unique=False, nullable=False)
    game_number = Column(String, unique=False, nullable=False)
    game_name = Column(String, unique=False, nullable=False)
    game_date = Column(DateTime, unique=False, nullable=False)
    home_team_id = Column(Integer, primary_key=False)
    away_team_id = Column(Integer, primary_key=False)
    home_team_score = Column(Integer, primary_key=False)
    away_team_score= Column(Integer, primary_key=False)
    winner_team_id= Column(Integer, primary_key=False)

class TeamGame(Base):
    __tablename__="team_game"
    team_game_id = Column(Integer, primary_key=True)
    team_id = Column(Integer, unique=True, nullable=False)
    game_id = Column(String, unique=True, nullable=False)
    result = Column(String, unique=True, nullable=False)
    home_away = Column(String, unique=True, nullable=False)

class PassingStats(Base):
    __tablename__="passing_stats"
    passingstats_id = Column(Integer, primary_key=True)
    team_game_id = Column(String, unique=True, nullable=False)
    yards = Column(String, unique=True, nullable=False)
    drives = Column(String, unique=True, nullable=False)
    turnovers = Column(String, unique=True, nullable=False)
    passes = Column(String, unique=True, nullable=False)
    yardsperpass = Column(String, unique=True, nullable=False)
    
def add_Teams(session):
    response=requests.get('https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/teams?limit=32').json()['items']
    teams=[]
    for i,r in enumerate(response):
        response=requests.get(r['$ref']).json()
        team=Team(team_id=response['id'],
                  team_location=response['location'],
             team_name=response['name'],
             logo_href=response['logos'][0]['href'],
             division=requests.get(response['groups']['$ref']).json()['name'])
        if int(response['id']) not in [t.team_id for t in session.query(Team).all()]:
            session.add(team)
            session.commit()
        
        
def add_Games(session):
    for team in session.query(Team).all():
        print(f'Processing {team.team_location + team.team_name}') 
        response=requests.get(f'https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2022/teams/{team.team_id}/events')
        for event in response.json()['items']:
            resp=requests.get(event['$ref']).json()
            game_id = resp['id']
            if game_id not in [g.game_id for g in session.query(Game).all()]:
                season_type = requests.get(resp['seasonType']['$ref']).json()['type']
                game_number = requests.get(resp['week']['$ref']).json()['number']
                game_name = resp['name']
                game_date = datetime.strptime(resp['date'],'%Y-%m-%dT%H:%MZ')
                if resp['competitions'][0]['competitors'][0]['homeAway']=='home':
                    home_team_id=resp['competitions'][0]['competitors'][0]['id']
                    home_team_score=requests.get(resp['competitions'][0]['competitors'][0]['score']['$ref']).json()['value']
                    away_team_id=resp['competitions'][0]['competitors'][1]['id']
                    away_team_score=requests.get(resp['competitions'][0]['competitors'][1]['score']['$ref']).json()['value']
                else:
                    home_team_id=resp['competitions'][0]['competitors'][1]['id']
                    home_team_score=requests.get(resp['competitions'][0]['competitors'][1]['score']['$ref']).json()['value']
                    away_team_id=resp['competitions'][0]['competitors'][0]['id']
                    away_team_score=requests.get(resp['competitions'][0]['competitors'][0]['score']['$ref']).json()['value']
                winner_team_id=home_team_id if home_team_score > away_team_score else away_team_id
                game=Game(game_id=game_id,
                          season_type=season_type,
                          game_number=game_number,
                          game_name=game_name,
                          game_date=game_date,
                          home_team_id=home_team_id,
                          away_team_id=away_team_id,
                          home_team_score=home_team_score,
                          away_team_score=away_team_score,
                          winner_team_id=winner_team_id
                         )
                session.add(game)
                session.commit()
                time.sleep(2)
            
Base.metadata.create_all(engine)
print('Adding Teams...')
add_Teams(session)
print('Adding Games...')
add_Games(session)
