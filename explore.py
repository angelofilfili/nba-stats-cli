from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats

# all_players = players.get_players()
# print(all_players[0])

# career = playercareerstats.PlayerCareerStats(player_id='2544')
# print(career.get_dict())

# career = playercareerstats.PlayerCareerStats(player_id='2544')
# df = career.season_totals_regular_season.get_data_frame()
# print(df.columns.tolist())
# print(df.tail(1))

# all_players = players.get_players()
# print(all_players[0])
# print(all_players[1])
# print(all_players[2])



player_stats = playercareerstats.PlayerCareerStats(player_id='2544')
player_dict = player_stats.get_dict()

print(player_dict.keys())
print(player_dict['resultSets'][0].keys())
print(player_dict['resultSets'][0]['rowSet'][-1])
print(player_dict['resultSets'][0]['headers'])