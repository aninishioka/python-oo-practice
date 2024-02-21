from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary.
        >>> wordFinder = WordFinder("words.txt")
        9 words read

        >>> wordFinder.random_word() in set(["# Veggies", "# Fruits", "", "kale", "parsnips", "apple", "mango"])
        True
    """
    def __init__(self, filepath):
        """Creates a WordFinder instance"""
        self.words = self.create_words_list(filepath)
        print(f"{len(self.words)} words read")

    def __repr__(self):
        """Returns representation of Word Finder instance."""
        return f"<{self.__class__.__name__} len(words)={len(self.words)}>"

    def create_words_list(self, filepath):
        """Creates a word list from each line from the text file."""
        words = []
        file = open(filepath)
        for line in file:
            words.append(line.strip())
        file.close()
        return words


    def random_word(self):
        """Returns a random word from the words list."""
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    """Special Word Finder: finds random words from a dictionary but ignores if
    it starts with # or a space."""

    def create_words_list(self, filepath):
        """Creates a word list from each line from the text file if the line
        does not starts with # or is blank."""
        words = super().create_words_list(filepath)
        return [word for word in words if not word.startswith('#') and word]

