from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    #TODO: Filepath!! word_list
    #TODO: repr
    def __init__(self, file):
        """Creates a WordFinder instance"""
        #TODO: Filepath =>word_list
        self.file = file
        self.word_list = []
        self.create_words_list()
        print(f"{len(self.word_list)} words read")

    def create_words_list(self):
        """Creates a word list from each line from the text file."""
        file = open(self.file)
        for line in file:
            #TODO: string method strip
            self.word_list.append(line.replace('\n', ''))
        file.close()


    def random_word(self):
        """Returns a random word from the words list."""
        return choice(self.word_list)


class SpecialWordFinder(WordFinder):
    """Special Word Finder: finds random words from a dictionary but ignores if
    it starts with # or a space."""
    def __init__(self, file):
        """Create a SpecialWordFinder instance"""
        super().__init__(file)
    #TODO: just add it to super class do not repeat
    def create_words_list(self):
        """Creates a word list from each line from the text file if the line
        does not starts with # or a space."""
        file = open(self.file)
        for line in file:
            if not line.startswith(("#", " ")):
                self.word_list.append(line.replace('\n', ''))
        file.close()

