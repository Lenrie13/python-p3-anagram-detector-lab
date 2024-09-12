# your code goes here!
class Anagram:
    def __init__(self, word):
        # Store the normalized form of the word
        self.original_word = word.lower()
        self.normalized_word = ''.join(sorted(self.original_word))
    
    def match(self, possible_anagrams):
        # Find and return all matching anagrams from the list
        matches = []
        for word in possible_anagrams:
            # Normalize the current word
            normalized = ''.join(sorted(word.lower()))
            # Check if normalized forms match
            if normalized == self.normalized_word and word.lower() != self.original_word:
                matches.append(word)
        return matches

anagram_checker = Anagram("listen")
print(anagram_checker.match(['enlists', 'google', 'inlets', 'banana']))  
