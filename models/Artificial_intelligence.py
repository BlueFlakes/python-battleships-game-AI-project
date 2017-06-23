from models.ocean import Ocean
from models.ship import Ship
import random


class Smart_ai:
    def __init__(self, enemy_ocean):
        self.best_shots = []
        self.used_shots = []
        self.add_second_stage = None
        self.enemy_ocean = enemy_ocean
        self.enemy_board = self.enemy_ocean.board
        self.enemy_ships = self.enemy_ocean.ships
        self.next_stage = None
        self.first_stage = None

    def set_first_stage(self):

        for i in range(10):
            self.best_shots.append(self.enemy_board[i][i])

            if i <= 5:
                self.best_shots.append(self.enemy_board[i][i + 4])
                self.best_shots.append(self.enemy_board[i + 4][i])

            if i <= 1:
                self.best_shots.append(self.enemy_board[i][i + 8])
                self.best_shots.append(self.enemy_board[i + 8][i])
        self.set_second_stage()

    def set_second_stage(self):
        all_shots = [shot for shot_list in [self.used_shots, self.best_shots] for shot in shot_list]
        best_shots = []

        for i in range(10):
            for j in range(10):
                if i % 2 == 0 and j % 2 == 0:
                    best_shots.append(self.enemy_board[i][j])
                elif (i + 1) % 2 == 0 and (j + 1) % 2 == 0:
                    best_shots.append(self.enemy_board[i][j])

        next_best_shots = [shot for shot in best_shots if shot not in all_shots]

        self.best_shots.extend(next_best_shots)

    def map(self):
        if self.first_stage is None:
            self.set_first_stage()
            self.first_stage = True

        if self.next_stage is None and self.are_two_biggest_ships_sunk():
            self.next_stage = True
            self.set_second_stage()

        self.best_shots = [shot for shot in self.best_shots if shot.__str__() not in ['.', 'x']]
        coordinate = random.choice(self.best_shots)
        self.used_shots.append(coordinate)
        self.best_shots.remove(coordinate)
        coords = None

        for i in range(10):
            for j in range(10):
                if coordinate == self.enemy_board[i][j]:
                    coords = [i, j]

            if coords:
                break

        return coords

    def are_two_biggest_ships_sunk(self):
        temp = []

        for ship in self.enemy_ships:
            if len(ship.squares) > 3:
                temp.append(ship)

        temp = False if False in [ship.is_sunk for ship in temp] else True

        return temp