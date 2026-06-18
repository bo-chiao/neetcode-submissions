class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        start_idx = ord("a")
        alphabet_map = {chr(i): i - start_idx for i in range(start_idx, start_idx + 26)}
        
        for string in strs:
            letter_count = [0] * 26
            for letter in string:
                letter_count[alphabet_map[letter]] += 1
            
            anagrams[tuple(letter_count)].append(string)
            
        return list(anagrams.values())