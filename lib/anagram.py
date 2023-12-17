class Anagram:
    def __init__(self, word):
        self.word = word.lower()
    
    def match(self, anagram_list):
        return [anagram for anagram in anagram_list if self.is_anagram(anagram)]
    
    def is_anagram(self, candidate):
        return candidate.lower() != self.word and sorted(candidate.lower()) == sorted(self.word)