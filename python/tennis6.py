class TennisGame6:
    player1_name: str
    player2_name: str
    player1_score: int
    player2_score: int

    def __init__(self, player1_name: str, player2_name: str) -> None:
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name: str) -> None:
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def _get_score_name(self, points: int, have_same_score: bool) -> str:
        score_name: str
        match points:
            case 0:
                score_name = "Love"
            case 1:
                score_name = "Fifteen"
            case 2:
                score_name = "Thirty"
            case _:
                if have_same_score:
                    score_name = "Deuce"
                else:
                    score_name = "Forty"
        if score_name != "Deuce" and have_same_score:
            score_name += "-All"
        return score_name

    def score(self):
        result: str
        have_same_score = self.player1_score == self.player2_score
        if have_same_score:
            result = self._get_score_name(self.player1_score, have_same_score)
        elif self.player1_score >= 4 or self.player2_score >= 4:
            # end-game score
            end_game_score: str
            diff_score = self.player1_score - self.player2_score
            match diff_score:
                case 1:
                    end_game_score = "Advantage " + self.player1_name
                case -1:
                    end_game_score = "Advantage " + self.player2_name
                case diff_score if diff_score >= 2:
                    end_game_score = "Win for " + self.player1_name
                case _:
                    end_game_score = "Win for " + self.player2_name

            result = end_game_score
        else:
            player1_score_name = self._get_score_name(
                self.player1_score, have_same_score
            )
            player2_score_name = self._get_score_name(
                self.player2_score, have_same_score
            )
            regular_score = player1_score_name + "-" + player2_score_name

            result = regular_score

        return result
