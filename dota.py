import http
import json
import requests


kill_threshold = 15

def get_match_data(match_id):

    #gets api from url
    r = requests.get('https://api.opendota.com/api/matches/' + str(match_id))


    playerData = [{"playerID": p["account_id"], "heroID": p["hero_id"], "isRadiant": p["isRadiant"]} for p in r.json()['players']]

    processedData = {
        "players": playerData,
        "matchID": r.json()["match_id"], 
        "matchDate": r.json()["start_time"], 
        "matchDuration": r.json()["duration"], 
        "radiantWon": r.json()["radiant_win"]}

    return processedData

def player_recent_matches(player_id):
    r = requests.get(f'https://api.opendota.com/api/players/{str(player_id)}/recentMatches')
    return [m["match_id"] for m in r.json()]

player_set = {1131498310, 99902951, 412806933}
names_of_players = {
    1131498310:"Havenfire", 
    99902951:"TheGuyWithTheHat", 
    412806933: "Fantôme"    
    }
cool_number = 6568791759

def recently_played(player_id_set):     
    
    total_list =  {match_id for player_id in player_id_set for match_id in player_recent_matches(player_id)}
    sorted_list = sorted(list(total_list))
    prepared_list = []
    for g in sorted_list:
        if g > cool_number:
            prepared_list.append(g)
    return prepared_list

def cool_stats(completed_match):

    total_data = requests.get('https://api.opendota.com/api/matches/' + str(completed_match))

    cool_stat_list = []

    player_index = []

    for i in range(10):
        if total_data.json()["players"][i]["account_id"] != None:
            if total_data.json()["players"][i]["account_id"] in player_set:
                player_index.append(i)
                
                
                player_string = ""
                player = total_data.json()["players"][i]
                player_accomplishment = []
                if kill_threshold < player["kills"]:
                    player_accomplishment.append("got over 15 kills")
                if "10" in player["kill_streaks"]:
                    player_accomplishment.append("went Beyond Godlike")
                elif "9" in player["kill_streaks"]:
                    player_accomplishment.append("went Godlike")
                if "5" in player["multi_kills"]:
                   player_accomplishment.append("had a Ramapge")
                if player["account_id"] == 412806933 and player["hero_id"] == 44 and player["lose"] == 1:
                    player_accomplishment.append(" should not have picked PA lul")

                if len(player_accomplishment) > 2:
                    player_accomplishment = player_accomplishment[:-2] + [", and ".join(player_accomplishment[-2:])]
                s = ", "
                if len(player_accomplishment) == 0:
                    pass
                else:
                    cool_stat_list.append(names_of_players[player["account_id"]] + " " + s.join(player_accomplishment))

    if total_data.json()["duration"] > 3600:
        cool_stat_list.append("Game was over an hour long!")
    

    return cool_stat_list


print(cool_stats(6572051338))
