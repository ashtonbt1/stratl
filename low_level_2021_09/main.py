import sqlalchemy as sa
from pathlib import Path

DB_FILEPATH = Path('../data_2021_09/strat.db')

sample_player = {
    'id': 'clemero01',
    'first_name': 'Roberto',
    'last_name': 'Clemente'
}

sample_hitter = {
    'id': 1,
    'player_id': 'clemero01',
    'first_name': 'Roberto',
    'last_name': 'Clemente',
    'season': 1960,
    'team': 'PIT',
    'bats': 'R',
    'auto_lead': False,
    'steal_grade': 'D',
    'good_lead': '4,6',
    'auto_cs': '10',
    'primary_steal': 13,
    'secondary_steal': 5,
    'bunt': 'B',
    'hnr': 'C',
    'running': 15,
    'power_lhp': 'N',
    'power_rhp': 'N'
}

def main():
    engine = sa.create_engine(f"sqlite:///{DB_FILEPATH}")
    with engine.connect() as conn:
        result = conn.execute(sa.text("select * from hitters"))
        for row in result:
            print(f"Name: {row['first_name']} {row['last_name']}")

def add_sample_record():
    engine = sa.create_engine(f"sqlite:///{DB_FILEPATH}")
    with engine.begin() as conn:
        conn.execute(f"INSERT INTO players ({','.join(sample_player.keys())}) VALUES ({','.join(sample_player.values())});")
        conn.execute("SELECT * from players")

if __name__ == '__main__':
    add_sample_record()
    main()