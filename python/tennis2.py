class TennisGame2:
    player1_name: str
    player2_name: str
    player1_points: int
    player2_points: int
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
            self.add_score_player1()
        else:
            self.add_score_player2()

    def _get_result(self) -> str:
        player1_score_name = self.POINTS_NAME[self.player1_points]
        player2_score_name = self.POINTS_NAME[self.player2_points]
        return player1_score_name + "-" + player2_score_name

    def score(self) -> str:
        result = ""
        have_same_points = self.player1_points == self.player2_points
        if have_same_points:
            if self.player1_points <= 2:
                result = self.POINTS_NAME[self.player1_points] + "-All"
            else:
                result = "Deuce"
        else:
            if self.player1_points < 4 and self.player2_points < 4:
                result = self._get_result()
            else:
                if self.player1_points > self.player2_points:
                    leader_name = self.player1_name
                else:
                    leader_name = self.player2_name

                abs_point_difference = abs((self.player1_points - self.player2_points))
                if abs_point_difference >= 2:
                    result = f"Win for {leader_name}"
                else:
                    result = f"Advantage {leader_name}"
        return result

    def set_add_score_player1(self, number: int) -> None:
        for i in range(number):
            self.add_score_player1()

    def set_add_score_player2(self, number: int) -> None:
        for i in range(number):
            self.add_score_player2()

    def add_score_player1(self) -> None:
        self.player1_points += 1

    def add_score_player2(self) -> None:
        self.player2_points += 1
