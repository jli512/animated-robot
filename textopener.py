import re
class WordCounter:
    def __init__(self, text, word):
        self.text1 = text
        self.word1 = word.lower()
        self.counter = 0
    def Counter(self):
        with open(self.text1, "r") as file:
            while True:
                line = file.readline().lower()
                letters = re.findall( r'\w+|[^\s\w]+', line)
                for words in letters:
                    if self.word1 == words:
                        self.counter += 1
                if not line:
                    print("There is", self.counter, "number of times that the word", "\"",self.word1,"\"", "occurs in this text.")
                    break


# Tests

Word1 = WordCounter("LICENSE.txt", "data")
Word1.Counter()



