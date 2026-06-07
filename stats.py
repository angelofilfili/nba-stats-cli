from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from player import Player

all_players = players.get_players()

def get_player_stats(player_name):
    for player in all_players:
        full_name = player['full_name']
        if full_name.lower() == player_name.lower():
            return player['id'], player['full_name']
    return None, None

def get_stats_by_id(player_id):
    player_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
    player_dict = player_stats.get_dict()
    headers = player_dict['resultSets'][0]['headers']
    numb_list = player_dict['resultSets'][0]['rowSet'][-1]
    return headers, numb_list

def build_player(player_name):

    player_id, official_name = get_player_stats(player_name)
    if player_id == None:
        return None
    id_code = player_id
    headers, numb_list = get_stats_by_id(player_id)

    gp_index = headers.index('GP')
    gp = numb_list[gp_index]
    if gp == 0:
        return "no_stats"

    ppg_index = headers.index('PTS')
    ppg = numb_list[ppg_index] / gp

    apg_index = headers.index('AST')
    apg = numb_list[apg_index] / gp

    rpg_index = headers.index('REB')
    rpg = numb_list[rpg_index] / gp

    spg_index = headers.index('STL')
    spg = numb_list[spg_index] / gp

    bpg_index = headers.index('BLK')
    bpg = numb_list[bpg_index] / gp

    mpg_index = headers.index('MIN')
    mpg = numb_list[mpg_index] / gp

    fg_index = headers.index('FG_PCT')
    fg_pct = numb_list[fg_index]

    threept_index = headers.index('FG3_PCT')
    three_pt_perc = numb_list[threept_index]

    season_index = headers.index('SEASON_ID')
    season = numb_list[season_index]

    return Player(official_name, id_code, ppg, rpg, apg, spg, bpg, mpg, fg_pct, three_pt_perc, season)