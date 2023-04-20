# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line


class Player:

    def __init__(self, name, speed, endurance, accuracy):
        # Raises a ValueError if the values are above 1
        if speed <= 0 or speed >= 1:
            raise ValueError("Speed must be betweeen 0 and 1")
        if endurance <= 0 or endurance >= 1:
            raise ValueError("Endurance must be betweeen 0 and 1")
        if accuracy <= 0 or accuracy >= 1:
            raise ValueError("Accuracy must be betweeen 0 and 1")

        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy

    def introduce(self):
        return f'Hello everyone, my name is {self.name}.'

    def strength(self):
        if self.speed > self.endurance and self.speed > self.accuracy:
            return ("speed", self.speed)
        elif self.endurance > self.speed and self.endurance > self.accuracy:
            return ("endurance", self.endurance)
        elif self.accuracy > self.speed and self.accuracy > self.endurance:
            return ("accuracy", self.accuracy)
        elif self.speed == self.endurance and self.speed != self.accuracy:
            return ("speed", self.speed, "endurance", self.endurance)
        elif self.speed == self.accuracy and self.speed != self.endurance:
            return ("speed", self.speed, "accuracy", self.accuracy)
        elif self.speed == self.endurance and self.speed == self.accuracy:
            return ("speed", self.speed, "endurance", self.endurance, "accuracy", self.accuracy)


player1 = Player('Rómulo', 0.8, 0.6, 0.9)
player2 = Player('Rafael', 0.9, 0.7, 0.8)
player3 = Player('Jason', 0.6, 0.6, 0.6)

print(player1.strength())
print(player2.strength())
print(player3.strength())


class Commentator:
    def __init__(self, name):
        self.name = name

    def sum_player(self, player):
        return player.speed + player.endurance + player.accuracy

    def compare_players(self, player1, player2, attribute):
        if getattr(player1, attribute) > getattr(player2, attribute):
            return player1.name
        elif getattr(player2, attribute) > getattr(player1, attribute):
            return player2.name

        elif getattr(player1, attribute) == getattr(player2, attribute):
            if player1.strength()[1] > player2.strength()[1]:
                return player1.name
            if player2.strength()[1] > player1.strength()[1]:
                return player2.name
            if player1.strength()[1] == player2.strength()[1]:
                if self.sum_player(player1) > self.sum_player(player2):
                    return player1.name
                if self.sum_player(player2) > self.sum_player(player1):
                    return player2.name
                return "These two players might as well be twins!"


ray = Commentator('Ray Hudson')
print(ray.compare_players(player1, player2, 'endurance'))
