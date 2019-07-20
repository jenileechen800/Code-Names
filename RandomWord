import random
from openpyxl import load_workbook


class RandomWord:
    wordList = []

    def __init__(self):
        self.fill_word_list()

    def get_random_word(self):
        return random.choice(self.wordList)

    def fill_word_list(self):
        wb = load_workbook(filename='TableWordlist.xlsx')
        ws = wb.get_sheet_by_name(name="Codenames")

        for row in ws.iter_rows():
            for cell in row:
                if not (cell.value is None):
                    self.wordList.append(cell.value)






