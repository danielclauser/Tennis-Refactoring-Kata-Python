class TennisGame1:
    player1_name: str
    player2_name: str
    player1_points: int
    player1_points: int
    POINTS_NAME: dict = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty",
    }

    def __init__(self, player1_name: str, player2_name: str) -> None:
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name: str) -> None:
        if player_name == self.player1_name:
            self.player1_points += 1
        else:
            self.player2_points += 1

    def score(self) -> str:
        result = ""
        temp_score = 0
        minus_result = self.player1_points - self.player2_points
        if minus_result == 0:
            if self.player1_points > 2:
                result = "Deuce"
            else:
                result = self.POINTS_NAME.get(self.player1_points) + "-All"
        elif self.player1_points >= 4 or self.player2_points >= 4:
            if minus_result > 0:
                leader_name = self.player1_name
            else:
                leader_name = self.player2_name
            if minus_result in (1, -1):
                result = f"Advantage {leader_name}"
            else:
                result = f"Win for {leader_name}"
        else:
                result += self.POINTS_NAME[self.player1_points]
                result += "-"
                result += self.POINTS_NAME[self.player2_points]
        return result
