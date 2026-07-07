class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        freq2 = {}
        for letter in s:
            freq1[letter] = freq1.get(letter,0)+1
        for letter in t:
            freq2[letter] = freq2.get(letter,0)+1
        if freq1 == freq2:
            return True
        else:
            return False