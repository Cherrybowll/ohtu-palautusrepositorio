class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        score = ""
        temp_score = 0

        if self.m_score1 >= 4 or self.m_score2 >= 4:
            score_diff = self._score_difference()

            if score_diff == 1:
                return f"Advantage {self.player1_name}"
            if score_diff == -1:
                return f"Advantage {self.player2_name}"
            if score_diff > 1:
                return f"Win for {self.player1_name}"
            if score_diff < -1:
                return f"Win for {self.player2_name}"

        player1_score_call = self._score_to_call_before_deuce(self.m_score1)
        player2_score_call = self._score_to_call_before_deuce(self.m_score2)

        if self._score_difference() == 0:
            if self.m_score1 > 2:
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
        return self.m_score1-self.m_score2
