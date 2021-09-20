from sqlalchemy import create_engine, text
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from pathlib import Path
from sqlalchemy.sql.expression import null, nullslast

from sqlalchemy.sql.sqltypes import Boolean

DB_FILEPATH = Path('../data_2021_09/strat.db')
metadata_obj = MetaData()

players_table = Table(
    'players',
    metadata_obj,
    Column('id', String, primary_key=True),
    Column('first_name', String, nullable=False),
    Column('last_name', String, nullable=False)
)

hitters_table = Table(
    'hitters',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('player_id', ForeignKey('players.id'), nullable=False,),
    Column('first_name', String, nullable=False),
    Column('last_name', String, nullable=False),
    Column('season', Integer, nullable=False),
    Column('team', String, nullable=False),
    Column('bats', String(1), nullable=False),
    Column('auto_lead', Boolean, nullable=False),
    Column('steal_grade', String, nullable=False),
    Column('good_lead', String, nullable=False),
    Column('auto_cs', String, nullable=False),
    Column('primary_steal', Integer, nullable=False),
    Column('secondary_steal', Integer, nullable=False),
    Column('bunt', String, nullable=False),
    Column('hnr', String, nullable=False),
    Column('running', Integer, nullable=False),
    Column('power_lhp', String, nullable=False),
    Column('power_rhp', String, nullable=False)
)

pitchers_table = Table(
    'pitchers',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('player_id', ForeignKey('players.id'), nullable=False,),
    Column('first_name', String, nullable=False),
    Column('last_name', String, nullable=False),
    Column('season', Integer, nullable=False),
    Column('team', String, nullable=False),
    Column('starter', Integer),
    Column('relief', Integer),
    Column('closer', String),
    Column('starter_first', Boolean),
    Column('starred', Boolean),
    Column('balk', Integer, nullable=False),
    Column('wp', Integer, nullable=False),
    Column('fielding', Integer, nullable=False),
    Column('error', Integer, nullable=False),
    Column('bats', String, nullable=False),
    Column('throws', String(1), nullable=False),
    Column('hold', Integer, nullable=False),
    Column('bunt', String, nullable=False),
    Column('hnr', String, nullable=False),
    Column('running', Integer, nullable=False),
    Column('power_lhp', String, nullable=False),
    Column('power_rhp', String, nullable=False),
    Column('auto_lead', Boolean),
    Column('steal_grade', String),
    Column('good_lead', String),
    Column('auto_cs', String),
    Column('primary_steal', Integer),
    Column('secondary_steal', Integer)
)

def setup():
    reset_everything = input("Running this command will wipe the DB and start fresh. Is that ok? [Y/N]")
    if reset_everything.lower() != 'y':
        print("Ok, quitting the setup function")
        return None
    engine = create_engine(f"sqlite:///{DB_FILEPATH}")
    metadata_obj.create_all(engine)

    

if __name__ == '__main__':
    setup()
    