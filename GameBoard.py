from GameObjects.Team import Team
from GameObjects.Cards.Card import Card
from random import shuffle
from tabulate import tabulate


class GameBoard:
    cardsDict = dict.fromkeys(list(range(0, 25)), 0)

    def __init__(self):
        self.generate_positions()

        self.cardsList = list(self.cardsDict.values())

    def show_user_cards(self):
        cardsWords = []

        for card in self.cardsList:
            cardsWords.append(getattr(card, "word"))

        row1 = cardsWords[0:5]
        row2 = cardsWords[5:10]
        row3 = cardsWords[10:15]
        row4 = cardsWords[15: 20]
        row5 = cardsWords[20:25]

        table = [row1, row2, row3, row4, row5]
        print(tabulate(table, tablefmt="grid"))

    def show_keymaster_cards(self):
        cardTypes = []

        for card in self.cardsList:
            cardTypes += getattr(card, "type")

        row1 = cardTypes[0:5]
        row2 = cardTypes[5:10]
        row3 = cardTypes[10:15]
        row4 = cardTypes[15: 20]
        row5 = cardTypes[20:25]

        table = [row1, row2, row3, row4, row5]
        print(tabulate(table, tablefmt="grid"))

    def generate_positions(self):

        all_pos = [[i] for i in range(25)]
        shuffle(all_pos)

        shuffled_all_pos = []

        for sublist in all_pos:
            for item in sublist:
                shuffled_all_pos.append(item)

        team_a_pos = shuffled_all_pos[0: 9]
        team_b_pos = shuffled_all_pos[9: 17]
        blank_pos = shuffled_all_pos[17: 24]
        assasin_pos = shuffled_all_pos[24]

        self.assign_positions(team_a_pos, team_b_pos, blank_pos)

    def assign_positions(self, team_a_pos, team_b_pos, blank_pos):
        # setattr(self.teamA, "positions", team_a_pos)
        # setattr(self.teamB, "positions", team_b_pos)

        for k in self.cardsDict.keys():
            if k in team_a_pos:
                self.cardsDict.update({k: Card("A")})
            elif k in team_b_pos:
                self.cardsDict.update({k: Card("B")})
            elif k in blank_pos:
                self.cardsDict.update({k: Card("O")})
            else:
                self.cardsDict.update({k: Card("X")})

    def game_over(self, losing_team):
        print("Game over!")
        for team in self.teamsList:
            if team is losing_team:
                print(team + " has lost the game:(")
            else:
                print(team + " has won the game:)")











