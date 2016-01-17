class Word1:
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
        for evil_pair in Word1.evil_pairs:
            if evil_pair in self._input:
                return True
        return False

    def _has_enough_vowels(self):
        vowels = 0
        for letter in Word1.vowels:
            vowels += self._input.count(letter)
        return vowels >= 3

class Word2:
    evil_pairs = ['ab', 'cd', 'pq', 'xy']
    vowels = 'aeiou'

    def __init__(self, input):
        self._input = input

    def is_nice(self):
        return self.has_non_overlapping_letter_pair() and self.has_oreo_pair()

    def has_non_overlapping_letter_pair(self):
        for i in range(0, len(self._input) - 3):
            pair = self._input[i:i+2]
            search_from = i+2
            if self._input.find(pair, search_from) >= 0:
                return True
        return False

    def has_oreo_pair(self):
        for i in range(0, len(self._input) - 2):
            left = self._input[i]
            right = self._input[i+2]
            if left == right:
                return True
        return False

class SantasList:
    def __init__(self, word_class, input):
        self._word_class = word_class
        self._words = input.splitlines()

    def nice_item_count(self):
        nice = [self._word_class(w).is_nice() for w in self._words]
        return nice.count(True)

if __name__ == "__main__":
    words = open('day5_input.txt', 'r').read()
    santas_first_list = SantasList(Word1, words)
    santas_second_list = SantasList(Word2, words)
    print("Santa's list has {0} nice entries according to part 1, but only {1} nice entries according to part 2.".format(santas_first_list.nice_item_count(), santas_second_list.nice_item_count()))