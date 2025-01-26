class TennisGame3:
    player1_name: str
    player2_name: str
    player1_points: int
    player2_points: int
    POINTS_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name: str, player2_name: str) -> None:
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, n: str) -> None:
        if n == "player1":
            self.player1_points += 1
        else:
            self.player2_points += 1

    def score(self) -> str:
        if (self.player1_points < 4 and self.player2_points < 4) and (
            self.player1_points + self.player2_points < 6
        ):
            player1_score = self.POINTS_NAMES[self.player1_points]
            player2_score = self.POINTS_NAMES[self.player2_points]
            if self.player1_points == self.player2_points:
                return player1_score + "-All"
            else:
                return player1_score + "-" + player2_score
        else:
            if self.player1_points == self.player2_points:
                return "Deuce"
            leader = (
                self.player1_name
                if self.player1_points > self.player2_points
                else self.player2_name
            )
            if (self.player1_points - self.player2_points) * (
                self.player1_points - self.player2_points
            ) == 1:
                return "Advantage " + leader
            else:
                return "Win for " + leader
