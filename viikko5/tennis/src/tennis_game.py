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

        if self.m_score1 == self.m_score2:
            if self.m_score1 == 0:
                score = "Love-All"
            elif self.m_score1 == 1:
                score = "Fifteen-All"
            elif self.m_score1 == 2:
                score = "Thirty-All"
            else:
                score = "Deuce"
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            minus_result = self.m_score1 - self. m_score2

            if minus_result == 1:
                score = f"Advantage {self.player1_name}"
            elif minus_result == -1:
                score = f"Advantage {self.player2_name}"
            elif minus_result >= 2:
                score = f"Win for {self.player1_name}"
            else:
                score = f"Win for {self.player2_name}"
        else:
            player1_score_call = self._score_to_call_before_deuce(self.m_score1)
            player2_score_call = self._score_to_call_before_deuce(self.m_score2)

            score = f"{player1_score_call}-{player2_score_call}"

        return score

    def _score_to_call_before_deuce(self, score):
        score_to_call_dict = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
            }
        return score_to_call_dict[score] if score < 4 else None