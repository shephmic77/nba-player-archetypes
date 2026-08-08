from nba_api.static import players
player_dict = players.get_players()
LeBron = [player for player in player_dict if player['full_name'] == 'Lebron James'][0]