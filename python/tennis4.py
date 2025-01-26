class TennisGame4:
    player1: str
    player2: str
    player1_score: int
    player2_score: int

    def __init__(self, player1_name, player2_name):
        self.player1 = player1_name
        self.player2 = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if self.player1 == player_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def score(self):
        dr = DefaultResult(self)
        advr = AdvantagePlayer2(self, dr)
        advs = AdvantagePlayer1(self, advr)
        gr = GamePlayer2(self, advs)
        gs = GamePlayer1(self, gr)
        result = Deuce(self, gs).get_result()
        return result.format()

    def player2_has_advantage(self):
        return (
            self.player2_score >= 4 and (self.player2_score - self.player1_score) == 1
        )

    def player1_has_advantage(self):
        return (
            self.player1_score >= 4 and (self.player1_score - self.player2_score) == 1
        )

    def player2_has_won(self):
        return (
            self.player2_score >= 4 and (self.player2_score - self.player1_score) >= 2
        )

    def player1_has_won(self):
        return (
            self.player1_score >= 4 and (self.player1_score - self.player2_score) >= 2
        )

    def is_deuce(self):
        return (
            self.player1_score >= 3
            and self.player2_score >= 3
            and (self.player1_score == self.player2_score)
        )


class TennisResult:
    def __init__(self, player1_score: int, player2_score: int) -> None:
        self.player1_score = player1_score
        self.player2_score = player2_score

    def format(self) -> str:
        if "" == self.player2_score:
            return self.player1_score
        if self.player1_score == self.player2_score:
            return self.player1_score + "-All"
        return self.player1_score + "-" + self.player2_score


class DefaultResult:
    def __init__(self, game) -> None:
        self.game = game
        self.scores = ["Love", "Fifteen", "Thirty", "Forty"]

    def get_result(self) -> TennisResult:
        return TennisResult(
            self.scores[self.game.player1_score], self.scores[self.game.player2_score]
        )


class AdvantagePlayer2:
    def __init__(self, game, next_result: DefaultResult):
        self.game = game
        self.next_result = next_result

    def get_result(self):
        if self.game.player2_has_advantage():
            return TennisResult("Advantage " + self.game.player2, "")
        return self.next_result.get_result()


class AdvantagePlayer1:
    def __init__(self, game, next_result: AdvantagePlayer2):
        self.game = game
        self.next_result = next_result

    def get_result(self):
        if self.game.player1_has_advantage():
            return TennisResult("Advantage " + self.game.player1, "")
        return self.next_result.get_result()


class GamePlayer2:
    def __init__(self, game, next_result: AdvantagePlayer1):
        self.game = game
        self.next_result = next_result

    def get_result(self):
        if self.game.player2_has_won():
            return TennisResult("Win for " + self.game.player2, "")
        return self.next_result.get_result()


class GamePlayer1:
    def __init__(self, game, next_result: GamePlayer2):
        self.game = game
        self.next_result = next_result

    def get_result(self):
        if self.game.player1_has_won():
            return TennisResult("Win for " + self.game.player1, "")
        return self.next_result.get_result()


class Deuce:
    def __init__(self, game, next_result: GamePlayer1):
        self.game = game
        self.next_result = next_result

    def get_result(self):
        if self.game.is_deuce():
            return TennisResult("Deuce", "")
        return self.next_result.get_result()
