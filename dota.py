import http
import json
import requests


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


player_recent_matches(1131498310)