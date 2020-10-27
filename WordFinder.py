from random import randrange

class WordFinder:

    def __init__(self, link):
        self.link = link
        self.word_list = []
        self.read_store()

    def read_store(self):
        file = open(self.link)
        for line in file:
            self.word_list.append(line)

    
    def random(self):
        print(self.word_list)

class SpecialWordFinder(WordFinder):

    def __init__(self, word_list):
        super().__init__(word_list)

    def read_store(self):
        super().read_store()
        sum = []
        [sum.append(x.strip()) for x in self.word_list if x != "\n" and x.find("#") < 0]
        print(self.word_list)
        print(sum)
        return self.word_list


