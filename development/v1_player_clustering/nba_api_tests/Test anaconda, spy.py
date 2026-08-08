# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
from nba_api.stats.static import players
player_dict = players.get_players()

bron = [player for player in player_dict if player['full_name'] == 'LeBron James'][0]
bron_id = bron['id']

from nba_api.stats.static import teams
team_dict = teams.get_teams()

GSW = [team for team in team_dict if team['full_name'] == 'Golden State Warriors'][0]
GSW_id = GSW['id']

from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll

gamelog_bron_all = playergamelog.PlayerGameLog(player_id='2544', season = SeasonAll.all)
gamelog_bron_df_all = gamelog_bron_all.get_data_frames()[0]

from nba_api.stats.endpoints import leaguegamefinder
GSW_games = leaguegamefinder.LeagueGameFinder(team_id_nullable=GSW_id).get_data_frames()[0]