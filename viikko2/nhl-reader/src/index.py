from playerreader import PlayerReader
from playerstats import PlayerStats
import rich.prompt

#Ei ehtinyt tehdä kunnon graafista käyttöliittymää. Lasketaanko silti? Toiminnallisuus löytyy.

def main():
    seasons = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]
    chosen_season = rich.prompt.Prompt.ask("Season:", choices=seasons)

    url = f"https://studies.cs.helsinki.fi/nhlstats/{chosen_season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    while True:
        nationalities = stats.get_nationalities()
        chosen_nationality = rich.prompt.Prompt.ask("Nationality:", choices=nationalities)

        players = stats.top_scorers_by_nationality(chosen_nationality)

        for player in players:
            print(player)


if __name__ == "__main__":
    main()
