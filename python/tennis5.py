class TennisGame5:
    player1_name: str
    player2_name: str
    player1_score: int
    player2_score: int
    POINTS_NAME: dict = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty",
    }

    def __init__(self, player1_name: str, player2_name: str) -> None:
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name: str) -> None | ValueError:
        if player_name == self.player1_name:
            self.player1_score += 1
        elif player_name == self.player2_name:
            self.player2_score += 1
        else:
            raise ValueError("Invalid player name.")

    def _get_score_name(self, points: int) -> str:
        if points < 4:
            return self.POINTS_NAME[points]
        else:
            return ""

    def _get_leader_name(self) -> str:
        if self.player1_score > self.player2_score:
            return self.player1_name
        else:
            return self.player2_name

    def score(self) -> str | ValueError:
        player1_score: str = self.player1_score
        player2_score: str = self.player2_score
        result: str = ""
        while player1_score > 4 or player2_score > 4:
            player1_score -= 1
            player2_score -= 1

        player1_score_name = self._get_score_name(player1_score)
        player2_score_name = self._get_score_name(player2_score)
        leader_name = self._get_leader_name()
        delta_score = abs(player1_score - player2_score)
        min_score = min(player1_score, player2_score)
        if delta_score == 0:
            if player1_score <= 2:
                result = player1_score_name + "-All"
            else:
                result = "Deuce"
        elif delta_score == 4 - min_score:
            if min_score < 3:
                result = f"Win for {leader_name}"
            else:
                result = f"Advantage {leader_name}"
        else:
            result = player1_score_name + "-" + player2_score_name
        return result
