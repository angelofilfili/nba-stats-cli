from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats

# all_players = players.get_players()
# print(all_players[0])

# career = playercareerstats.PlayerCareerStats(player_id='2544')
# print(career.get_dict())

career = playercareerstats.PlayerCareerStats(player_id='2544')
df = career.season_totals_regular_season.get_data_frame()
print(df.columns.tolist())
print(df.tail(1))