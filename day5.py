class Word:
    evil_pairs = ['ab', 'cd', 'pq', 'xy']
    vowels = 'aeiou'

    def __init__(self, input):
        self._input = input

    def is_nice(self):
        if not self.has_double_letters():
            return False
        if self._has_evil_pairs():
            return False
        return self._has_enough_vowels();

    def has_double_letters(self):
        for i in range(0, len(self._input) - 1):
            if self._input[i] == self._input[i+1]:
                return True
        return False

    def _has_evil_pairs(self):
        for letters in Word.evil_pairs:
            if self._input.find(letters) >= 0:
                return True
        return False

    def _has_enough_vowels(self):
        vowels = 0
        for letter in Word.vowels:
            vowels += self._input.count(letter)
        return vowels >= 3

class SantasList:
    def __init__(self, input):
        self._words = input.splitlines()

    def nice_item_count(self):
        nice = [Word(w).is_nice() for w in self._words]
        return nice.count(True)

if __name__ == "__main__":
    words = open('day5_input.txt', 'r').read()
    santas_list = SantasList(words)
    print("Santa's list has {0} nice entries.".format(santas_list.nice_item_count()))