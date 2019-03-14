# Cody Dzierzon
# 3-19
# Farkle
import random


class Die(object):

    def __init__(self):
        self.value = 1
        self.selected = False

    def roll(self):
        self.value = random.randint(1, 6)

    def select(self):
        self.selected = True

    def deselect(self):
        self.selected = False

    def display_value(self):
        if self.selected:
            return str(self.value) + " - selected"
        else:
            return str(self.value)


class Player(object):

    def __init__(self, name):
        self.score = 0
        self.name = name

    def sayHi(self):
        print("Hi, my name is " + self.name)

    def take_turn(self):
        turn = Turn(self)
        while turn.active == True:
            turn.roll()

        self.score += turn.score


class Score(object):

    def __init__(self, dice):
        self.value = 0
        self.farkle = False

        self.ones = 0
        self.twos = 0
        self.threes = 0
        self.fours = 0
        self.fives = 0
        self.sixes = 0
        for die in dice:
            if die.selected and die.value == 1:
                self.ones += 1
            elif die.selected and die.value == 2:
                self.twos += 1
            elif die.selected and die.value == 3:
                self.threes += 1
            elif die.selected and die.value == 4:
                self.fours += 1
            elif die.selected and die.value == 5:
                self.fives += 1
            elif die.selected and die.value == 6:
                self.sixes += 1
        if self.check6straight() or self.check3pairs():
            return
        self.check_ones()
        self.check_fives()
        self.check_2346()
        self.check_farkle()

    def check6straight(self):
        if self.ones == 6 or self.twos == 6 or self.threes == 6 or self.fours == 6 or self.fives == 6 or self.sixes == 6:
            self.value = 1000
            return True
        return False

    def check3pairs(self):
        num_pairs = 0
        if self.ones == 2: num_pairs += 1
        if self.twos == 2: num_pairs += 1
        if self.threes == 2: num_pairs += 1
        if self.fours == 2: num_pairs += 1
        if self.fives == 2: num_pairs += 1
        if self.sixes == 2: num_pairs += 1
        return num_pairs == 3

    def check_ones(self):
        num_ones = self.ones
        if num_ones >= 3:
            self.value += 1000
            num_ones -= 3
        self.value += num_ones * 100

    def check_fives(self):
        num_fives = self.fives
        if num_fives >= 3:
            self.value += 500
            num_fives -= 3
        self.value += num_fives * 50

    def check_2346(self):
        if self.twos >= 3: self.value += 200
        if self.threes >= 3: self.value += 300
        if self.fours >= 3: self.value += 400
        if self.sixes >= 3: self.value += 600

    def check_farkle(self):
        self.farkle = self.value == 0


class Turn(object):

    def __init__(self, player):
        self.dice = [Die(), Die(), Die(), Die(), Die(), Die()]
        self.selected_dice = []
        self.score = 0
        self.roll_score = 0
        self.roll_number = 0
        self.active = True
        self.player = player

    def roll(self):
        for i in range(0, len(self.dice)):
            die = self.dice[i]
            die.roll()
        self.display_values()

    def display_values(self):
        print("")
        print("Player: " + self.player.name)
        print("Total Score: " + str(self.player.score))
        print("Roll Score: " + str(self.score + self.roll_score))
        print("rolled dice:")
        for i in range(0, len(self.dice)):
            die = self.dice[i]
            message = str(i + 1) + ": " + die.display_value()
            print(message)

        print("used dice:")
        for i in range(0, len(self.selected_dice)):
            die = self.selected_dice[i]
            message = str(i + 1) + ": " + die.display_value()
            print(message)

        print("")
        answer = raw_input("enter die number, r to roll, t to take the points, or p to pass: ").lower()
        if answer == "p":
            self.active = False
            self.score = 0

        elif answer == "t":
            self.score += self.roll_score
            self.active = False

        elif answer == "r":
            self.score += self.roll_score
            self.take()
            self.roll()

        elif answer == "1" or answer == "2" or answer == "3" or answer == "4" or answer == "5" or answer == "6":
            index = int(answer)
            self.select(index)


    def score_roll(self):
        roll_score = Score(self.dice)
        self.roll_score = roll_score.value
        if roll_score.farkle: self.active = False


    def take(self):
        selected = []
        for die in self.dice:
            if die.selected:
                die.deselect()
                selected.append(die)
                self.selected_dice.append(die)

        for die in selected:
            self.dice.remove(die)


    def select(self, num):
        self.dice[num - 1].selected = True
        self.score_roll()
        self.display_values()

    def deselect(self, num):
        self.dice[num - 1].selected = False
        self.score_roll()
        self.display_values()


class Game(object):

    def __init__(self):
        self.players = []
        self.high_scorer = Player("")
        self.is_winning_round = False

    def play(self):
        num_players = input("How many players would you like to have? ")
        for i in range(0, num_players):
            name = raw_input("enter name for player " + str(i+1) + ": ")
            player = Player(name)
            self.players.append(player)

        while self.is_winning_round == False:
            for player in self.players:
                player.take_turn()
                if player.score >= 1500:
                    self.is_winning_round = True
                if player.score > self.high_scorer.score:
                    self.high_scorer = player

        print(self.high_scorer.name + " wins! ")
        print(str(self.high_scorer.score) + " points")



def main():
    print("rules")
    play = raw_input("would you like to play? (y/n) ").lower()
    while play == "y":
        game = Game()
        game.play()
        play = raw_input("would you like to play again? (y/n) ").lower()

    print("Thanks for your support :)")



main()