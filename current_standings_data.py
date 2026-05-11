import datetime
import sys
import os

import statsapi
import pandas as pd


sys.path.append(r"C:\Users\ryana\portfolio")

from utils.sql import write_to_sql

standings_for_today = statsapi.standings_data(leagueId="103,104", division="all", include_wildcard=True, season=None, standingsTypes=None, date=None)



div_keys = list(standings_for_today.keys())

new_dict = {}

for key in div_keys:
    new_dict[standings_for_today[key]['div_name']] = standings_for_today[key]['teams']

standings_for_df = []

for key, value in new_dict.items():
    for e in new_dict[key]:
        e['division'] = key
        e['time'] = datetime.datetime.now()
        standings_for_df.append(e)

# Convert to DataFrame for local backup
standings_for_df = pd.DataFrame(standings_for_df)

write_to_sql(standings_for_df, 'mlb.daily_standings')

csv_file_path = r"C:\Users\ryana\portfolio\mlb-etl\standings.csv"

# Writing locally in case of sql problems
try:
    all_standings = pd.read_csv(csv_file_path)
    all_standings = pd.concat([all_standings, standings_for_df])
    all_standings.to_csv(csv_file_path)
except FileNotFoundError:
    standings_for_df = pd.DataFrame(standings_for_df)
    standings_for_df.to_csv(csv_file_path)
