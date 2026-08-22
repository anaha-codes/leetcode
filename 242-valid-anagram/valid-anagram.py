class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = {}
        anagram1 = {}
        for value in s:
            anagram[value] = anagram.get(value,0)+1

        for value in t:
            anagram1[value] = anagram1.get(value,0)+1

        return anagram == anagram1