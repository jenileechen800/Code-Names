import time

class Team:
    def __init__(self, type, gameBoard):
        self.type = type
        self.positions = []
        self.gameBoard = gameBoard
        self.cardsDict = gameBoard.cardsDict
        self.num_flipped = 0
        self.spymaster = ""

    def increment_num_flipped(self):
        self.num_flipped += 1

    def has_won(self):
        return self.num_flipped == len(self.positions)

    def turn(self, other_team):
        self.show_cards()
        self.spymaster_clues()
        self.team_guesses(other_team)
        self.show_scoreboard(other_team)

    def spymaster_clues(self):
        print("Spymaster \"" + self.spymaster + "\" it is your turn! You have 1 minute to think of your clues!")

        self.line_break()
        sm_total_guesses = input(">>>Spymaster " + self.spymaster + "<<< enter total clues\n")
        self.line_break()
        sm_clue = input(">>>Spymaster" + self.spymaster + "<<< enter (comma-separated) single-word clues\n")

        guesses_list = sm_clue.strip().split(",")

        print(len(guesses_list))

        while len(guesses_list) != int(sm_total_guesses):
            self.line_break()
            print("\n\n>>>Spymaster, you must enter the same number of"
                  " word-clues as the number of code names to guess<<<")

            sm_clue = input("Spymaster, enter (comma-separated) single-word clues\n")

            guesses_list = sm_clue.strip().split(",")

        self.line_break()
        print("\"Team " + self.type + "\"" + " you have " + sm_total_guesses + " codename cards to flip!")
        print("Here are the hints!")
        print(guesses_list)

    def team_guesses(self, other_team):
        self.line_break()
        self.gameBoard.show_user_cards()
        self.line_break()

        team_guesses = input("\"Team " + self.type + "\" please enter word guess for every spymaster clue (comma-separated)\n")

        team_guesses = team_guesses.strip().split(",")

        for guess in team_guesses:
            guess.lower()

        for guessed_word in team_guesses:
            for card in self.cardsDict.values():
                card_word = getattr(card, "word").lower()
                if card_word == guessed_word:
                    card.flip_card()
                    if getattr(card, "type") == self.type:
                        self.increment_num_flipped()
                    elif getattr(card, "type") == other_team.type:
                        other_team.increment_num_flipped()
                    elif getattr(card, "type") == "X":
                        print("Assassin card flipped :0")
                        return "Game Over", self.type

    def show_scoreboard(self, other_team):
        self.gameBoard.show_user_cards()
        print("\"Team " + self.type + "\" has a total of: " + str(self.num_flipped) + " of " + str(len(self.positions)) + " cards flipped")
        print("\"Team " + other_team.type + "\" has a total of: " + str(getattr(other_team, "num_flipped")) + " of " + str(len(getattr(other_team, "positions"))) + " cards flipped")

    def show_cards(self):
        self.line_break()
        self.gameBoard.show_keymaster_cards()
        self.gameBoard.show_user_cards()
        self.line_break()

    def line_break(self):
        print("============================================================")








    


