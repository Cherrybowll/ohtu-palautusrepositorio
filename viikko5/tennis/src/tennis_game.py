class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        if self.player1_score >= 4 or self.player2_score >= 4:
            score_diff = self._score_difference()

            if score_diff == 1:
                return f"Advantage {self.player1_name}"
            if score_diff == -1:
                return f"Advantage {self.player2_name}"
            if score_diff > 1:
                return f"Win for {self.player1_name}"
            if score_diff < -1:
                return f"Win for {self.player2_name}"

        player1_score_call = self._score_to_call_before_deuce(self.player1_score)
        player2_score_call = self._score_to_call_before_deuce(self.player2_score)

        if self._score_difference() == 0:
            if self.player1_score > 2:
                return "Deuce"

            return f"{player1_score_call}-All"

        return f"{player1_score_call}-{player2_score_call}"


    def _score_to_call_before_deuce(self, score):
        score_to_call_dict = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
            }
        return score_to_call_dict[score] if score < 4 else None
    
    def _score_difference(self):
        return self.player1_score-self.player2_score
