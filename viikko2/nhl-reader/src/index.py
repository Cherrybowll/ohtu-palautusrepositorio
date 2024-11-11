import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print("Players from FIN\n")
    sorted_fin_players = sorted(filter(nationality, players), reverse=True, key=sort_by_points)
    for player in sorted_fin_players:
            print(player)

def nationality(player):
    return player.nationality == "FIN"

def sort_by_points(player):
    return player.goals+player.assists

if __name__ == "__main__":
    main()
