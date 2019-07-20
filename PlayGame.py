from GameObjects.GameBoard import GameBoard
from GameObjects.Team import Team


class PlayGame:
    gameboard = GameBoard()
    teamA = Team("A", gameboard)
    teamB = Team("B", gameboard)

    def text_intro(self):
        print("Welcome to Code Names!\n")

        instructions = input("Would you like to read the instructions? (y/n)\n")

        if instructions is "y":
            print("Every round, your spymaster will give your team a hint"
                  "and a number of cards to flip. Your team will input"
                  "your guess into the game system. The cards will be flipped, resulting"
                  "in either your team losing (the assasin card), getting closer to"
                  "winning (your team's card), getting farther from winning (your"
                  "opponent's card), or nothing (blank card). "

                  "Both teams will take turns guessing and flipping cards until a team"
                  "has flipped all their cards -> winning the game."
                  "The goal of the game is to 'flip' all of your team's cards"
                  "before the other team. Beware - flipping the 'ASSASSIN' card"
                  "will result in an automatic loss."
                  ""
                  "Begin by splitting into two teams and choosing a spymaster.")

        self.choose_spymaster()
        print("Good luck! Ready, set, CODE NAMES!")

    def choose_spymaster(self):
        setattr(self.teamA, "spymaster", input("Team A, enter your spy master's name: \n"))
        setattr(self.teamB, "spymaster", input("Team B, enter your spy master's name: \n"))

    def play(self):
        self.text_intro()
        self.teamA.turn(self.teamB)

        # while not(self.teamA.has_won() or self.teamB.has_won()):
        #     self.teamA.turn(self.teamB)
        #     self.teamB.turn(self.teamA)


playGame = PlayGame()

playGame.play()


