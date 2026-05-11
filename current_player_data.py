import datetime
import sys

import statsapi
import pandas as pd
from pandantic import Pandantic

from models.models import DailyHittingRow, DailyPitchingRow, DailyFieldingRow

sys.path.append(r"C:\Users\ryana\portfolio")

from utils.sql import write_to_sql


CURRENT_YEAR = datetime.date.today().year
# How often the script prints its progress
VERBOSITY = 1

players = statsapi.get('sports_players',{'season':CURRENT_YEAR})['people']

for side, data_model in zip(['hitting', 'pitching', 'fielding'], 
                            [DailyHittingRow, DailyPitchingRow, DailyFieldingRow]):

    full_player_stats = pd.DataFrame()
    
    print(f"Getting {side} now")
    TABLE_NAME = f"mlb.daily_{side}"

    for i, l in enumerate(players):

        id = l['id']
        stats = pd.DataFrame(statsapi.player_stat_data(id, group=side, type="season"))

        # Flattening stats nested dict
        flattened_stats = pd.json_normalize(stats['stats'])
        stats = pd.concat([stats, flattened_stats], axis=1).drop('stats', axis=1)

        stats.rename(columns=lambda x: x.replace('stats.', '') if x.startswith('stats.') else x, inplace=True)

        full_player_stats = pd.concat([full_player_stats, stats])

        if i % VERBOSITY == 0:
            print(f"Players scraped: {i}")

    full_player_stats['time'] = datetime.datetime.now()
    full_player_stats = full_player_stats.reset_index(drop=True)

    # Initialize validator
    # Pandantic allows for pydantic model validation
    # on pandas dataframes directly
    validator = Pandantic(schema=data_model)
    full_player_stats_coerced = validator.validate(full_player_stats)

    write_to_sql(full_player_stats, TABLE_NAME)