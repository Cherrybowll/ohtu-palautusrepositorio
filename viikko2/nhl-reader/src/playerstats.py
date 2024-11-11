class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()
    
    def top_scorers_by_nationality(self, nationality):
        #What a beautiful one-liner amirite
        return sorted(filter(lambda player: player.nationality==nationality, self.players), reverse=True, key=lambda player: player.goals+player.assists)