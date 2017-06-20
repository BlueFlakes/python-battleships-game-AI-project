class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.is_over = self.is_game_over()

    def __init__(self, player, computer):
        self.player1 = player
        self.player2 = computer
        self.is_over = self.is_game_over()

    def __init__(self, computer1, computer2):
        self.player1 = computer1
        self.player2 = computer2
        self.is_over = self.is_game_over()

    def is_game_over(self):
        if self.player1.check_status() == True or self.player2.check_status() == True:
            return True
