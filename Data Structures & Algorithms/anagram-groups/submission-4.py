class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        start_idx = ord("a")
        alphabet_map = {chr(i): i - start_idx for i in range(start_idx, start_idx + 26)}
        
        for string in strs:
            letter_count = [0] * 26
            for letter in string:
                letter_count[alphabet_map[letter]] += 1
            if tuple(letter_count) in anagrams:
                anagrams[tuple(letter_count)].append(string)
            else:
                anagrams[tuple(letter_count)] = [string]
        return list(anagrams.values())
            